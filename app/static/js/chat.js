const STORAGE_MESSAGES = "chat_messages";
const STORAGE_THEME = "chat_theme";

const chatBox = document.getElementById("chat-box");
const input = document.getElementById("message");
const typing = document.getElementById("typing-indicator");
const toggle = document.getElementById("theme-toggle");
const endButton = document.getElementById("end-chat");

///// CLIENT SESSION STATE
// Load persisted state
let messages = JSON.parse(localStorage.getItem(STORAGE_MESSAGES)) || [];
let theme = localStorage.getItem(STORAGE_THEME) || "light";

// Initial restore
restoreTheme();
restoreMessages();

// Restore messages to DOM
function restoreMessages() {
  chatBox.innerHTML = "";
  messages.forEach(m => appendMessage(m.role, m.content));
}

// Restore theme
function restoreTheme() {
  document.body.classList.toggle("dark", theme === "dark");
  toggle.textContent = theme === "dark" ? "☀️" : "🌙";
}

// Send user message
async function sendMessage() {
  const text = input.value.trim();
  if (!text) return;

  input.value = "";

  const userMessage = { role: "user", content: text };
  messages.push(userMessage);
  persistMessages();
  appendMessage("user", text);
  showTyping(true);

  try {
    // Send FULL conversation (recommended)
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages })
    });

    if (!res.ok) throw new Error("Backend error");

    const data = await res.json();

    const assistantMessage = {
      role: "assistant",
      content: data.reply
    };

    messages.push(assistantMessage);
    persistMessages();
    appendMessage("assistant", data.reply);

    // If sleep tool invoked → finalize
    if (data.tool === "sleep") {
      await endConversation();
    }

  } catch (err) {
    appendMessage("system", "⚠️ Error contacting AI backend.");
  } finally {
    showTyping(false);
  }
}

// Append message to DOM
function appendMessage(role, text) {
  const msg = document.createElement("div");
  msg.className = `message ${role}`;
  msg.textContent = text;

  const time = document.createElement("div");
  time.className = "timestamp";
  time.textContent = new Date().toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit"
  });

  msg.appendChild(time);
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

// Typing indicator
function showTyping(show) {
  typing.classList.toggle("hidden", !show);
}

// Theme toggle (browser-only)
toggle.onclick = () => {
  theme = theme === "dark" ? "light" : "dark";
  document.body.classList.toggle("dark", theme === "dark");
  toggle.textContent = theme === "dark" ? "☀️" : "🌙";
  localStorage.setItem(STORAGE_THEME, theme);
};

// Persist messages
function persistMessages() {
  localStorage.setItem(STORAGE_MESSAGES, JSON.stringify(messages));
}

// End chat → consolidate full conversation
async function endConversation() {
  if (!messages.length) return;

  await fetch("/api/consolidate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ messages })
  });

  localStorage.removeItem(STORAGE_MESSAGES);
  messages = [];
  chatBox.innerHTML = "";
}

// Enter-to-send
input.addEventListener("keydown", e => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

// Bind End Chat button
endButton.onclick = endConversation;

