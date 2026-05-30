export async function onRequest(context) {
  const BACKEND = context.env.BACKEND_URL;
  const url = new URL(context.request.url);
  const target = `${BACKEND}${url.pathname}${url.search}`;

  const init = {
    method: context.request.method,
    headers: new Headers(context.request.headers),
  };

  if (context.request.method !== "GET" && context.request.method !== "HEAD") {
    init.body = context.request.body;
  }

  const response = await fetch(target, init);

  return new Response(response.body, {
    status: response.status,
    headers: response.headers,
  });
}
