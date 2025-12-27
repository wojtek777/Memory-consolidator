let sessionId = null;
const chatBox = document.getElementById("chat-box");

async function initSession() {
  const res = await fetch("/api/session", { method: "POST" });
  const data = await res.json();
  sessionId = data.session_id;
}

async function sendMessage() {
  const input = document.getElementById("message");
  const text = input.value;
  input.value = "";

  appendMessage("user", text);

  const res = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ session_id: sessionId, message: text })
  });

  const data = await res.json();
  appendMessage("assistant", data.reply);
}

function appendMessage(role, text) {
  const div = document.createElement("div");
  div.textContent = `${role}: ${text}`;
  chatBox.appendChild(div);
}

initSession();

