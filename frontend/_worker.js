// The site is unlisted — shared by private link, never advertised. This is sent on
// every response (see the two set() calls below) so that assets which cannot carry
// a <meta robots> tag are still excluded from search indexes.
const NOINDEX = "noindex, nofollow, noarchive, nosnippet, noimageindex";

const BLOCKED_PATTERN =
  /(?:^\/\.env|^\/\.git|\/wp-admin|\/wp-login|\/wp-includes|\/xmlrpc\.php|\/wp-content|\/\.aws|\/\.ssh|\/\.DS_Store|\/config\.json$|\/\.htaccess|\/\.htpasswd|\/administrator|\/phpmyadmin|\/cgi-bin)/i;

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname.replace(/\/+/g, "/");

    if (BLOCKED_PATTERN.test(path)) {
      return new Response("Not Found", { status: 404 });
    }

    const isApi = url.pathname.startsWith("/api/");
    const isMcp = url.pathname === "/mcp" || url.pathname.startsWith("/mcp/");
    if (isApi || isMcp) {
      const backend = env.BACKEND_URL;
      if (!backend) {
        return new Response("Backend not configured", { status: 502 });
      }

      // Normalize /mcp -> /mcp/ here: the backend would otherwise 307-redirect
      // with the Cloud Run host in Location, bypassing this proxy.
      const targetPath = url.pathname === "/mcp" ? "/mcp/" : url.pathname;
      const target = `${backend}${targetPath}${url.search}`;
      const headers = new Headers(request.headers);
      if (env.PROXY_SECRET) {
        headers.set("X-Proxy-Secret", env.PROXY_SECRET);
      }

      // Forward the visitor's real IP for per-user rate limiting: the backend
      // only sees this Worker as the TCP peer. Delete first so a client-sent
      // X-Client-IP can never pass through.
      headers.delete("X-Client-IP");
      const clientIp = request.headers.get("CF-Connecting-IP");
      if (clientIp) {
        headers.set("X-Client-IP", clientIp);
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

      responseHeaders.set("X-Robots-Tag", NOINDEX);

      return new Response(response.body, {
        status: response.status,
        headers: responseHeaders,
      });
    }

    // Static assets. The HTML pages carry their own <meta robots>, but images,
    // CSS, JS, and robots.txt itself can only be marked via the header — so it
    // is set here, on everything the site serves. Copying the response through
    // `new Response(body, res)` is what makes the headers mutable, and it keeps
    // a null-body status (304 on a conditional request) intact.
    const assetResponse = await env.ASSETS.fetch(request);
    const out = new Response(assetResponse.body, assetResponse);
    out.headers.set("X-Robots-Tag", NOINDEX);
    return out;
  },
};
