from app.ai.client import GPTClient
from app.ai.prompts import MEMORY_CUTTER_PROMPT, IDENTITY_STACK_PROMPT
import json

class ChatService:
    def __init__(self):
        self.gpt = GPTClient()

    def reply(self, messages):
        """
        messages: list of dicts [{role, content}]
        """
        return self.gpt.chat(messages)


    # -----------------------------
    # Memory condensation
    # -----------------------------
    def condense_memory(self, messages):
        conversation_text = "\n".join(f"{m['role'].upper()}: {m['content']}" for m in messages)
        prompt = MEMORY_CUTTER_PROMPT.format(conversation=conversation_text)
        response = self.client.query(prompt)
        memories = json.loads(response)
        return memories

    # -----------------------------
    # Identity stack creation
    # -----------------------------
    def create_identity_stack(self, messages):
        conversation_text = "\n".join(f"{m['role'].upper()}: {m['content']}" for m in messages)
        prompt = IDENTITY_STACK_PROMPT.format(conversation=conversation_text)
        response = self.client.query(prompt)
        identity_stack = json.loads(response)
        return identity_stack

