const BLOCKED_PATTERN =
  /(?:^\/\.env|^\/\.git|\/wp-admin|\/wp-login|\/wp-includes|\/xmlrpc\.php|\/wp-content|\/\.aws|\/\.ssh|\/\.DS_Store|\/config\.json$|\/\.htaccess|\/\.htpasswd|\/administrator|\/phpmyadmin|\/cgi-bin)/i;

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname.replace(/\/+/g, "/");

    if (BLOCKED_PATTERN.test(path)) {
      return new Response("Not Found", { status: 404 });
    }

    if (url.pathname.startsWith("/api/")) {
      const backend = env.BACKEND_URL;
      if (!backend) {
        return new Response("Backend not configured", { status: 502 });
      }

      const target = `${backend}${url.pathname}${url.search}`;
      const headers = new Headers(request.headers);
      if (env.PROXY_SECRET) {
        headers.set("X-Proxy-Secret", env.PROXY_SECRET);
      }

      const init = { method: request.method, headers };
      if (request.method !== "GET" && request.method !== "HEAD") {
        init.body = request.body;
      }

      const response = await fetch(target, init);
      const responseHeaders = new Headers(response.headers);
      responseHeaders.delete("access-control-allow-origin");
      responseHeaders.delete("access-control-allow-methods");
      responseHeaders.delete("access-control-allow-headers");

      return new Response(response.body, {
        status: response.status,
        headers: responseHeaders,
      });
    }

    return env.ASSETS.fetch(request);
  },
};
