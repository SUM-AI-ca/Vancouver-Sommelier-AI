/* BC Wine AI — SSE chat client */

const TOOL_LABELS = {
  search_bcliquor_tool: "BC Liquor inventory",
  search_winealign_tool: "WineAlign critic reviews",
  search_everything_wine_tool: "Everything Wine availability",
  search_okanagan_cellars_tool: "Okanagan Cellars stock",
  search_marquis_tool: "Marquis Wine Cellars",
  search_tavily_tool: "Web reference",
  search_gismondi_tool: "Gismondi tasting notes",
  search_robert_parker_tool: "Robert Parker ratings",
  reasoning_pair_wine_tool: "Sommelier reasoning",
  update_preferences_tool: "Saving preferences",
};

const $ = (sel) => document.querySelector(sel);
const messagesEl = $("#chat-messages");
const inputEl = $("#chat-input");
const sendBtn = $("#chat-send");
const typingEl = $("#chat-typing");
const overlay = $("#chat-overlay");

let threadId = localStorage.getItem("bc_wine_thread_id");
let sending = false;

/* ── Session ─────────────────────────────────────── */

async function ensureSession() {
  if (threadId) return;
  try {
    const res = await fetch("/api/session", { method: "POST" });
    const data = await res.json();
    threadId = data.thread_id;
    localStorage.setItem("bc_wine_thread_id", threadId);
  } catch {
    threadId = crypto.randomUUID();
    localStorage.setItem("bc_wine_thread_id", threadId);
  }
}

/* ── Chat overlay toggle ─────────────────────────── */

function openChat() {
  overlay.classList.add("active");
  inputEl.focus();
}

function closeChat() {
  overlay.classList.remove("active");
}

$("#open-chat").addEventListener("click", openChat);
$("#nav-chat").addEventListener("click", (e) => {
  e.preventDefault();
  openChat();
});
$("#chat-close").addEventListener("click", closeChat);

overlay.addEventListener("click", (e) => {
  if (e.target === overlay) closeChat();
});

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") closeChat();
});

/* ── Message rendering ───────────────────────────── */

function addMessage(role, html) {
  const div = document.createElement("div");
  div.className = `demo-chat-message ${role}`;
  div.innerHTML = html;
  messagesEl.appendChild(div);
  scrollToBottom();
  return div;
}

function addToolBadge(toolName) {
  const label = TOOL_LABELS[toolName] || toolName;
  const badge = document.createElement("div");
  badge.className = "tool-badge";
  badge.dataset.tool = toolName;
  badge.innerHTML = `<span class="spinner"></span>${label}`;
  messagesEl.appendChild(badge);
  scrollToBottom();
  return badge;
}

function completeToolBadge(toolName) {
  const badges = messagesEl.querySelectorAll(
    `.tool-badge[data-tool="${toolName}"]:not(.done)`
  );
  badges.forEach((b) => b.classList.add("done"));
}

function scrollToBottom() {
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

/* ── Send message via SSE ────────────────────────── */

async function sendMessage() {
  const text = inputEl.value.trim();
  if (!text || sending) return;

  sending = true;
  sendBtn.disabled = true;
  inputEl.value = "";
  inputEl.style.height = "auto";

  addMessage("user", escapeHtml(text));

  await ensureSession();

  typingEl.classList.add("visible");
  let aiDiv = null;
  let tokenBuf = "";

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ thread_id: threadId, message: text }),
    });

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
          case "tool_start":
            addToolBadge(event.tool);
            break;

          case "tool_end":
            completeToolBadge(event.tool);
            break;

          case "token":
            typingEl.classList.remove("visible");
            if (!aiDiv) {
              aiDiv = addMessage("ai", "");
            }
            tokenBuf += event.text;
            aiDiv.innerHTML = renderMarkdown(tokenBuf);
            scrollToBottom();
            break;

          case "done":
            typingEl.classList.remove("visible");
            if (aiDiv) {
              aiDiv.innerHTML = renderMarkdown(tokenBuf);
            }
            break;

          case "error":
            typingEl.classList.remove("visible");
            addMessage("ai", `<em>Error: ${escapeHtml(event.message)}</em>`);
            break;
        }
      }
    }
  } catch (err) {
    typingEl.classList.remove("visible");
    addMessage("ai", `<em>Connection error. Please try again.</em>`);
  }

  sending = false;
  sendBtn.disabled = false;
  inputEl.focus();
}

/* ── Markdown & utilities ────────────────────────── */

function renderMarkdown(text) {
  if (typeof marked !== "undefined" && marked.parse) {
    return marked.parse(text);
  }
  return escapeHtml(text).replace(/\n/g, "<br>");
}

function escapeHtml(str) {
  const map = { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" };
  return str.replace(/[&<>"']/g, (c) => map[c]);
}

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
  inputEl.style.height = Math.min(inputEl.scrollHeight, 120) + "px";
});

ensureSession();
