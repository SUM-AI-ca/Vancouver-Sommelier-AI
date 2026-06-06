/* Vancouver Drinks AI — SSE chat client */

const API_BASE = "";

const TURNSTILE_SITE_KEY = "0x4AAAAAACk40fbVxvRdolMx";
// Turnstile site keys are domain-bound and won't issue a token on localhost, which
// stalls the send. Skip the widget in local dev; production (real hostname) is unchanged.
// The backend already bypasses verification when CF_TURNSTILE_SECRET is unset (local).
const TURNSTILE_DISABLED = ["localhost", "127.0.0.1", "0.0.0.0", ""].includes(location.hostname);
let turnstileToken = null;
let turnstileWidgetId = null;

// Inject the Cloudflare Turnstile script only in production, after window.initTurnstile
// is defined. Loading it statically with ?onload=initTurnstile raced app.js (the async
// script could fire its onload before initTurnstile existed -> "Unable to find onload
// callback" error). On localhost we never load it, so the widget is fully skipped.
function loadTurnstile() {
  if (TURNSTILE_DISABLED) return;
  if (document.querySelector("script[data-turnstile]")) return;
  window.initTurnstile = initTurnstile;
  const s = document.createElement("script");
  s.src = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=initTurnstile";
  s.async = true;
  s.defer = true;
  s.setAttribute("data-turnstile", "");
  document.head.appendChild(s);
}

function initTurnstile() {
  if (TURNSTILE_DISABLED) return;
  if (typeof turnstile === "undefined" || document.getElementById("cf-turnstile")) return;
  const container = document.getElementById("turnstile-container");
  if (!container) return;
  turnstileWidgetId = turnstile.render(container, {
    sitekey: TURNSTILE_SITE_KEY,
    callback: (token) => { turnstileToken = token; },
    "refresh-expired": "auto",
    size: "normal",
  });
}

async function getTurnstileToken() {
  if (TURNSTILE_DISABLED) return null;
  if (typeof turnstile === "undefined") return null;
  for (let i = 0; i < 20; i++) {
    if (turnstileToken) {
      const token = turnstileToken;
      turnstileToken = null;
      turnstile.reset(turnstileWidgetId);
      return token;
    }
    await new Promise((r) => setTimeout(r, 250));
  }
  return null;
}

const AGENT_TOOL_NAMES = new Set([
  "sourcing_agent_tool",
  "sommelier_agent_tool",
  "menu_architect_tool",
]);

const TOOL_LABELS = {
  sourcing_agent_tool: "Sourcing Agent",
  sommelier_agent_tool: "Sommelier",
  menu_architect_tool: "Menu Architect",
  search_bcliquor_tool: "BC Liquor Store",
  search_everything_wine_tool: "Everything Wine",
  search_okanagan_cellars_tool: "Okanagan Cellars",
  search_suttonplace_tool: "Sutton Place Wine Merchant",
  search_marquis_tool: "Marquis Wine Cellars",
  search_legacy_liquor_store_tool: "Legacy Liquor Store",
  reasoning_pair_wine_tool: "Wine Pairing",
  update_preferences_tool: "Preferences",
  ask_user_clarification_tool: "Clarification",
  vision: "Image analysis",
};

const $ = (sel) => document.querySelector(sel);
const messagesEl = $("#chat-messages");
const inputEl = $("#chat-input");
const sendBtn = $("#chat-send");
const statusEl = $("#chat-status");
const overlay = $("#chat-overlay");
const openBtn = $("#open-chat");
const closeBtn = $("#chat-close");
const attachBtn = $("#chat-attach");
const fileInput = $("#chat-file");
const attachmentsEl = $("#chat-attachments");

const MAX_IMAGES = 2;
const MAX_DIM = 2048; // longest edge, px — high enough for small wine-list text
let attachedImages = []; // data-URL strings, pending send

// thread_id is intentionally NOT persisted in localStorage. Each time the
// chatbox is opened we create a fresh session so the agent's wine_context
// cache (which accumulates across turns inside a thread) starts empty —
// this prevents wines from earlier unrelated queries from leaking into a
// new conversation. Follow-up turns within the same open chat still share
// memory because the thread_id stays stable until the chat is closed.
let threadId = null;
let sending = false;
let activeTools = 0;

const INITIAL_GREETING = "Ask about drinks in Vancouver: wine, beer, spirits, cider — prices, availability, food pairings, or anything else.";

/* ── Overlay open/close ──────────────────────────── */

async function openChat() {
  resetConversation();
  overlay.classList.add("active");
  document.body.style.overflow = "hidden";
  await ensureSession();
  setTimeout(() => inputEl.focus(), 0);
}

loadTurnstile();

function closeChat() {
  overlay.classList.remove("active");
  document.body.style.overflow = "";
}

function resetConversation() {
  threadId = null;
  activeTools = 0;
  clearAttachments();
  messagesEl.innerHTML = `<div class="chat-message ai">${escapeHtml(INITIAL_GREETING)}</div>`;
  setStatus("Ready", false);
}

openBtn.addEventListener("click", openChat);
closeBtn.addEventListener("click", closeChat);

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && overlay.classList.contains("active")) closeChat();
});

/* ── Session ─────────────────────────────────────── */

async function ensureSession() {
  if (threadId) return;
  try {
    const res = await fetch(`${API_BASE}/api/session`, { method: "POST" });
    const data = await res.json();
    threadId = data.thread_id;
  } catch {
    threadId = crypto.randomUUID();
  }
}

/* ── Status ──────────────────────────────────────── */

function setStatus(text, working) {
  statusEl.textContent = text;
  statusEl.classList.toggle("is-working", !!working);
}

/* ── Message rendering ───────────────────────────── */

function addMessage(role, html) {
  const div = document.createElement("div");
  div.className = `chat-message ${role}`;
  div.innerHTML = html;
  messagesEl.appendChild(div);
  scrollToBottom();
  return div;
}

function addToolBadge(toolName, runId) {
  const label = TOOL_LABELS[toolName] || toolName;
  const wrapper = document.createElement("div");
  wrapper.className = "tool-badge";
  wrapper.dataset.tool = toolName;
  if (runId) wrapper.dataset.runId = runId;
  wrapper.innerHTML = `
    <button type="button" class="tool-badge-header" aria-expanded="false">
      <span class="tool-badge-indicator" aria-hidden="true"></span>
      <span class="tool-badge-label">${escapeHtml(label)}</span>
      <span class="tool-badge-count"></span>
      <span class="tool-badge-chevron" aria-hidden="true"></span>
    </button>
    <div class="tool-badge-panel"></div>
  `;
  const headerBtn = wrapper.querySelector(".tool-badge-header");
  headerBtn.addEventListener("click", () => {
    if (!wrapper.classList.contains("done")) return;
    const expanded = wrapper.classList.toggle("open");
    headerBtn.setAttribute("aria-expanded", expanded ? "true" : "false");
  });
  messagesEl.appendChild(wrapper);
  scrollToBottom();
  return wrapper;
}

function renderToolRow(row) {
  const title = escapeHtml(row.title || "");
  // Long-form bodies (sommelier reasoning, web grounding) come through with
  // markdown:true so they render with paragraphs/lists instead of getting
  // clipped into a single subtitle line.
  if (row.markdown && row.body) {
    return `<div class="tool-row">
              <div class="tool-row-title">${title}</div>
              <div class="tool-row-body">${renderMarkdown(row.body)}</div>
            </div>`;
  }
  const subtitle = row.subtitle
    ? `<span class="tool-row-subtitle">${escapeHtml(row.subtitle)}</span>`
    : "";
  if (row.url) {
    return `<a class="tool-row" href="${escapeAttr(row.url)}" target="_blank" rel="noopener noreferrer">
              <span class="tool-row-title">${title}</span>${subtitle}
            </a>`;
  }
  return `<div class="tool-row">
            <span class="tool-row-title">${title}</span>${subtitle}
          </div>`;
}

function completeToolBadge(toolName, runId, summary, count) {
  let target = null;
  if (runId) {
    target = messagesEl.querySelector(
      `.tool-badge[data-run-id="${CSS.escape(runId)}"]`
    );
  }
  if (!target) {
    target = messagesEl.querySelector(
      `.tool-badge[data-tool="${CSS.escape(toolName)}"]:not(.done)`
    );
  }
  if (!target) return;

  target.classList.add("done");
  const countEl = target.querySelector(".tool-badge-count");
  if (countEl) {
    countEl.textContent = count ? `${count} result${count > 1 ? "s" : ""}` : "no results";
  }
  const panel = target.querySelector(".tool-badge-panel");
  if (panel && Array.isArray(summary) && summary.length > 0) {
    panel.innerHTML = summary.map(renderToolRow).join("");
  } else if (panel) {
    panel.innerHTML = `<div class="tool-row-empty">No results returned.</div>`;
  }
}

function addAgentBox(toolName, runId) {
  const label = TOOL_LABELS[toolName] || toolName;
  const wrapper = document.createElement("div");
  wrapper.className = "agent-box";
  wrapper.dataset.tool = toolName;
  if (runId) wrapper.dataset.runId = runId;
  wrapper.innerHTML = `
    <button type="button" class="agent-box-header" aria-expanded="false">
      <span class="agent-box-indicator" aria-hidden="true"></span>
      <span class="agent-box-label">${escapeHtml(label)}</span>
      <span class="agent-box-status">working…</span>
      <span class="agent-box-chevron" aria-hidden="true"></span>
    </button>
    <div class="agent-box-panel"></div>
  `;
  const headerBtn = wrapper.querySelector(".agent-box-header");
  headerBtn.addEventListener("click", () => {
    if (!wrapper.classList.contains("done")) return;
    const expanded = wrapper.classList.toggle("open");
    headerBtn.setAttribute("aria-expanded", expanded ? "true" : "false");
  });
  messagesEl.appendChild(wrapper);
  scrollToBottom();
  return wrapper;
}

function completeAgentBox(toolName, runId, innerTools) {
  let target = runId
    ? messagesEl.querySelector(`.agent-box[data-run-id="${CSS.escape(runId)}"]`)
    : null;
  if (!target) {
    target = messagesEl.querySelector(
      `.agent-box[data-tool="${CSS.escape(toolName)}"]:not(.done)`
    );
  }
  if (!target) return;

  target.classList.add("done");

  const tools = Array.isArray(innerTools) ? innerTools : [];
  const totalResults = tools.reduce((s, t) => s + (t.count || 0), 0);
  const sources = tools.filter((t) => t.count > 0).length;

  const statusEl = target.querySelector(".agent-box-status");
  if (statusEl) {
    statusEl.textContent = totalResults
      ? `${totalResults} result${totalResults > 1 ? "s" : ""} from ${sources} source${sources > 1 ? "s" : ""}`
      : "completed";
  }

  const panel = target.querySelector(".agent-box-panel");
  if (panel && tools.length > 0) {
    panel.innerHTML = tools.map((t) => {
      const tLabel = escapeHtml(t.label || TOOL_LABELS[t.tool] || t.tool || "Tool");
      const tCount = t.count || 0;
      const countText = tCount ? `${tCount} result${tCount > 1 ? "s" : ""}` : "no results";
      const rows = Array.isArray(t.summary) && t.summary.length > 0
        ? t.summary.map(renderToolRow).join("")
        : `<div class="tool-row-empty">No results returned.</div>`;
      return `
        <div class="inner-tool-group">
          <button type="button" class="inner-tool-header" aria-expanded="false">
            <span class="inner-tool-dot"></span>
            <span class="inner-tool-label">${tLabel}</span>
            <span class="inner-tool-count">${escapeHtml(countText)}</span>
            <span class="inner-tool-chevron"></span>
          </button>
          <div class="inner-tool-panel">${rows}</div>
        </div>
      `;
    }).join("");

    panel.querySelectorAll(".inner-tool-header").forEach((btn) => {
      btn.addEventListener("click", () => {
        const group = btn.closest(".inner-tool-group");
        const expanded = group.classList.toggle("open");
        btn.setAttribute("aria-expanded", expanded ? "true" : "false");
      });
    });
  } else if (panel) {
    panel.innerHTML = `<div class="tool-row-empty">No details available.</div>`;
  }
}

function markRemainingBadgesDone() {
  messagesEl.querySelectorAll(".tool-badge:not(.done), .agent-box:not(.done)").forEach((b) => {
    b.classList.add("done");
    const countEl = b.querySelector(".tool-badge-count") || b.querySelector(".agent-box-status");
    if (countEl) countEl.textContent = "completed";
    const panel = b.querySelector(".tool-badge-panel") || b.querySelector(".agent-box-panel");
    if (panel && !panel.innerHTML) {
      panel.innerHTML = `<div class="tool-row-empty">No details available.</div>`;
    }
  });
}

function scrollToBottom() {
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

function renderClarification(question, options) {
  const container = document.createElement("div");
  container.className = "chat-message ai clarification active";

  const q = document.createElement("div");
  q.className = "clarification-question";
  q.textContent = question;
  container.appendChild(q);

  if (Array.isArray(options) && options.length > 0) {
    const opts = document.createElement("div");
    opts.className = "clarification-options";
    for (const opt of options) {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "clarification-option-btn";
      btn.textContent = opt;
      btn.addEventListener("click", () => {
        if (sending) return;
        inputEl.value = opt;
        sendMessage();
      });
      opts.appendChild(btn);
    }
    container.appendChild(opts);
  }

  const hint = document.createElement("div");
  hint.className = "clarification-hint";
  hint.textContent = options && options.length > 0
    ? "Pick one or type your own answer below."
    : "Type your answer below.";
  container.appendChild(hint);

  messagesEl.appendChild(container);
  scrollToBottom();
}

/* ── Image attachments ───────────────────────────── */

// Decode a file, downscale its longest edge to MAX_DIM, and re-encode as JPEG.
// Resolves to a data-URL, or null if the browser can't decode the file (e.g.
// HEIC on desktop Chrome/Firefox — iOS Safari decodes it natively and succeeds).
function downscaleToDataUrl(file) {
  return new Promise((resolve) => {
    const url = URL.createObjectURL(file);
    const img = new Image();
    img.onload = () => {
      URL.revokeObjectURL(url);
      const longest = Math.max(img.width, img.height) || 1;
      const scale = longest > MAX_DIM ? MAX_DIM / longest : 1;
      const w = Math.max(1, Math.round(img.width * scale));
      const h = Math.max(1, Math.round(img.height * scale));
      const canvas = document.createElement("canvas");
      canvas.width = w;
      canvas.height = h;
      canvas.getContext("2d").drawImage(img, 0, 0, w, h);
      try {
        resolve(canvas.toDataURL("image/jpeg", 0.85));
      } catch {
        resolve(null);
      }
    };
    img.onerror = () => {
      URL.revokeObjectURL(url);
      resolve(null);
    };
    img.src = url;
  });
}

async function processFiles(fileList) {
  const files = Array.from(fileList || []).filter((f) => f.type.startsWith("image/"));
  for (const file of files) {
    if (attachedImages.length >= MAX_IMAGES) {
      alert(`이미지는 한 번에 최대 ${MAX_IMAGES}장까지 첨부할 수 있어요.`);
      break;
    }
    const dataUrl = await downscaleToDataUrl(file);
    if (dataUrl) {
      attachedImages.push(dataUrl);
      renderAttachments();
    } else {
      alert("이 이미지를 불러올 수 없어요. JPEG 또는 PNG로 다시 시도해주세요.");
    }
  }
}

function renderAttachments() {
  if (!attachedImages.length) {
    attachmentsEl.hidden = true;
    attachmentsEl.innerHTML = "";
    return;
  }
  attachmentsEl.hidden = false;
  attachmentsEl.innerHTML = attachedImages
    .map(
      (u, i) => `<div class="chat-attachment">
        <img src="${u}" alt="attachment ${i + 1}">
        <button type="button" class="chat-attachment-remove" data-index="${i}" aria-label="Remove image">&times;</button>
      </div>`
    )
    .join("");
  attachmentsEl.querySelectorAll(".chat-attachment-remove").forEach((btn) => {
    btn.addEventListener("click", () => {
      attachedImages.splice(Number(btn.dataset.index), 1);
      renderAttachments();
    });
  });
}

function clearAttachments() {
  attachedImages = [];
  if (attachmentsEl) {
    attachmentsEl.hidden = true;
    attachmentsEl.innerHTML = "";
  }
}

/* ── Send message via SSE ────────────────────────── */

async function sendMessage() {
  const text = inputEl.value.trim();
  const images = attachedImages.slice();
  if ((!text && images.length === 0) || sending) return;

  sending = true;
  sendBtn.disabled = true;
  inputEl.value = "";
  inputEl.style.height = "auto";
  clearAttachments();

  const thumbsHtml = images.length
    ? `<div class="chat-msg-thumbs">${images
        .map((u) => `<img class="chat-msg-thumb" src="${u}" alt="attached image">`)
        .join("")}</div>`
    : "";
  addMessage("user", (text ? escapeHtml(text) : "") + thumbsHtml);

  await ensureSession();

  activeTools = 0;
  setStatus("Processing", true);
  let aiDiv = null;
  let tokenBuf = "";
  let currentRunId = null;

  try {
    async function doChat() {
      const cfToken = await getTurnstileToken();
      return fetch(`${API_BASE}/api/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          thread_id: threadId,
          message: text,
          images: images.length ? images : undefined,
          cf_turnstile_token: cfToken,
        }),
      });
    }

    let res = await doChat();
    if (res.status === 403) {
      res = await doChat();
    }

    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });
      const lines = buffer.split("\n");
      buffer = lines.pop();

      for (const line of lines) {
        if (!line.startsWith("data: ")) continue;
        let event;
        try {
          event = JSON.parse(line.slice(6));
        } catch {
          continue;
        }

        switch (event.type) {
          case "vision_start":
            // vision_node runs before any tool. Reuse the tool-badge UI so the
            // "Image analysis" step shows the same expandable result panel.
            addToolBadge("vision", null);
            setStatus("Analyzing image", true);
            break;

          case "vision_result":
            completeToolBadge("vision", null, event.summary, event.count);
            setStatus("Processing", true);
            break;

          case "tool_start": {
            if (!AGENT_TOOL_NAMES.has(event.tool)) break;
            addAgentBox(event.tool, event.run_id);
            activeTools += 1;
            const label = TOOL_LABELS[event.tool] || event.tool;
            setStatus(`Running ${label}`, true);
            break;
          }

          case "tool_end":
            if (!AGENT_TOOL_NAMES.has(event.tool)) break;
            completeAgentBox(event.tool, event.run_id, event.inner_tools);
            activeTools = Math.max(0, activeTools - 1);
            if (activeTools === 0) setStatus("Processing", true);
            break;

          case "token":
            if (event.run_id && event.run_id !== currentRunId) {
              currentRunId = event.run_id;
              tokenBuf = "";
              if (aiDiv) {
                aiDiv.remove();
                aiDiv = null;
              }
            }
            if (!aiDiv) {
              aiDiv = addMessage("ai", "");
              setStatus("Writing response", true);
            }
            tokenBuf += event.text;
            aiDiv.innerHTML = renderMarkdown(tokenBuf);
            scrollToBottom();
            break;

          case "clarification_request":
            // Disable any in-flight prior clarification chips so only the
            // most recent question is actionable.
            messagesEl.querySelectorAll(".clarification.active").forEach((el) => {
              el.classList.remove("active");
              el.querySelectorAll(".clarification-option-btn").forEach((b) => (b.disabled = true));
            });
            renderClarification(event.question, event.options || []);
            setStatus("Waiting for your reply", false);
            break;

          case "done":
            if (aiDiv) {
              aiDiv.innerHTML = renderMarkdown(tokenBuf);
            }
            markRemainingBadgesDone();
            setStatus("Task finished", false);
            break;

          case "error":
            addMessage("ai", `<em>Error: ${escapeHtml(event.message)}</em>`);
            setStatus("Error", false);
            break;
        }
      }
    }
  } catch (err) {
    addMessage("ai", `<em>Connection error. Please try again.</em>`);
    setStatus("Error", false);
  }

  sending = false;
  sendBtn.disabled = false;
  inputEl.focus();
}

/* ── Markdown & utilities ────────────────────────── */

function renderMarkdown(text) {
  if (typeof marked !== "undefined" && marked.parse) {
    const html = marked.parse(text);
    return html.replace(
      /<a (?![^>]*\btarget=)/gi,
      '<a target="_blank" rel="noopener noreferrer" ',
    );
  }
  return escapeHtml(text).replace(/\n/g, "<br>");
}

function escapeHtml(str) {
  if (str == null) return "";
  const map = { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" };
  return String(str).replace(/[&<>"']/g, (c) => map[c]);
}

function escapeAttr(str) {
  const s = String(str || "");
  if (/^\s*javascript:/i.test(s)) return "#";
  return s.replace(/["'<>]/g, (c) => ({ '"': "&quot;", "'": "&#039;", "<": "&lt;", ">": "&gt;" }[c]));
}

/* ── Save as PDF ────────────────────────────────── */

function saveAsPdf() {
  const messages = messagesEl.querySelectorAll(".chat-message");
  if (!messages.length) return;

  const lines = [];
  messages.forEach((el) => {
    const isUser = el.classList.contains("user");
    const role = isUser ? "You" : "Drinks AI";
    lines.push(`<div class="pdf-msg ${isUser ? "pdf-user" : "pdf-ai"}"><span class="pdf-role">${role}</span>${el.innerHTML}</div>`);
  });

  const html = `<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Vancouver Drinks AI — Conversation</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'DM Sans',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:#2A1F22;padding:2rem;max-width:800px;margin:0 auto;line-height:1.6}
h1{font-size:1.3rem;font-weight:700;color:#7A3D4F;margin-bottom:0.25rem}
.pdf-date{font-size:0.8rem;color:#998A8C;margin-bottom:2rem;padding-bottom:1rem;border-bottom:1px solid #ECDFE0}
.pdf-msg{margin-bottom:1.25rem;padding:0.75rem 1rem;border-radius:8px}
.pdf-user{background:#F4E7E9}
.pdf-ai{background:#FBF6F6}
.pdf-role{display:block;font-weight:700;font-size:0.8rem;text-transform:uppercase;letter-spacing:0.03em;margin-bottom:0.35rem;color:#7A3D4F}
.pdf-tool{font-size:0.8rem;color:#6B5B5E;padding:0.3rem 0;margin-left:1rem;font-style:italic}
.pdf-msg p{margin-bottom:0.5rem}
.pdf-msg ul,.pdf-msg ol{margin:0.5rem 0 0.5rem 1.5rem}
.pdf-msg table{border-collapse:collapse;width:100%;margin:0.5rem 0;font-size:0.85rem}
.pdf-msg th,.pdf-msg td{border:1px solid #ECDFE0;padding:0.4rem 0.6rem;text-align:left}
.pdf-msg th{background:#F4E7E9;font-weight:600}
.pdf-msg a{color:#7A3D4F}
.pdf-msg h1,.pdf-msg h2,.pdf-msg h3{font-size:1rem;font-weight:700;margin:0.75rem 0 0.25rem}
.chat-msg-thumbs{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}
.chat-msg-thumb{width:auto;height:auto;max-width:220px;max-height:220px;object-fit:contain;border-radius:6px;border:1px solid #ECDFE0}
.pdf-msg img{max-width:100%;height:auto}
</style></head><body>
<h1>Vancouver Drinks AI</h1>
<div class="pdf-date">${new Date().toLocaleDateString("en-CA", { year: "numeric", month: "long", day: "numeric", hour: "2-digit", minute: "2-digit" })}</div>
${lines.join("\n")}
</body></html>`;

  const w = window.open("", "_blank");
  if (!w) {
    alert("Please allow pop-ups to save as PDF.");
    return;
  }
  w.document.write(html);
  w.document.close();
  w.onafterprint = () => w.close();
  setTimeout(() => w.print(), 300);
}

const savePdfBtn = $("#chat-save-pdf");
if (savePdfBtn) savePdfBtn.addEventListener("click", saveAsPdf);

/* ── Event listeners ─────────────────────────────── */

sendBtn.addEventListener("click", sendMessage);

inputEl.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

inputEl.addEventListener("input", () => {
  inputEl.style.height = "auto";
  inputEl.style.height = Math.min(inputEl.scrollHeight, 140) + "px";
});

/* ── Image attachment listeners ──────────────────── */

if (attachBtn && fileInput) {
  attachBtn.addEventListener("click", () => fileInput.click());
  fileInput.addEventListener("change", (e) => {
    processFiles(e.target.files);
    fileInput.value = ""; // allow re-selecting the same file
  });
}

// Paste an image straight from the clipboard.
inputEl.addEventListener("paste", (e) => {
  const items = e.clipboardData && e.clipboardData.items;
  if (!items) return;
  const files = [];
  for (const it of items) {
    if (it.kind === "file" && it.type.startsWith("image/")) {
      const f = it.getAsFile();
      if (f) files.push(f);
    }
  }
  if (files.length) {
    e.preventDefault();
    processFiles(files);
  }
});

// Drag-and-drop anywhere on the chat overlay.
["dragover", "dragenter"].forEach((ev) =>
  overlay.addEventListener(ev, (e) => {
    if (e.dataTransfer && Array.from(e.dataTransfer.types || []).includes("Files")) {
      e.preventDefault();
      overlay.classList.add("drag-over");
    }
  })
);
["dragleave", "dragend", "drop"].forEach((ev) =>
  overlay.addEventListener(ev, () => overlay.classList.remove("drag-over"))
);
overlay.addEventListener("drop", (e) => {
  if (e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files.length) {
    e.preventDefault();
    processFiles(e.dataTransfer.files);
  }
});

// Clean up the stale thread_id from earlier builds that persisted it across
// reloads. No-op for new visitors.
try { localStorage.removeItem("bc_wine_thread_id"); } catch {}
