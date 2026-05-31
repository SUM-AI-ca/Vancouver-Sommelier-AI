const DEFAULT_BACKEND = "https://bc-wine-agent-135257828500.us-west1.run.app";
const DEFAULT_SECRET = "Lk9s7vR7SzB3k3ag1mcMuxFtPe8NQ4fqcmPBiKCfEVM";

export async function onRequest(context) {
  const BACKEND = context.env.BACKEND_URL || DEFAULT_BACKEND;
  const SECRET = context.env.PROXY_SECRET || DEFAULT_SECRET;

  if (!BACKEND) {
    return new Response("Backend not configured", { status: 502 });
  }

  const url = new URL(context.request.url);
  const target = `${BACKEND}${url.pathname}${url.search}`;

  const headers = new Headers(context.request.headers);
  if (SECRET) {
    headers.set("X-Proxy-Secret", SECRET);
  }

  const init = {
    method: context.request.method,
    headers,
  };

  if (context.request.method !== "GET" && context.request.method !== "HEAD") {
    init.body = context.request.body;
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
