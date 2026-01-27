from app.ai.client import GPTClient
from app.ai.prompts import MEMORY_CUTTER_PROMPT
from app.ai.prompts import IDENTITY_PROMPT


class MemoryCutterService:
    def __init__(self):
        self.gpt = GPTClient()

    def cut(self, messages):
        response = self.gpt.chat(
            messages,
            system_prompt=MEMORY_CUTTER_PROMPT
        )
        return response  # structured JSON (important)


class IdentityService:
    def __init__(self):
        self.gpt = GPTClient()

    def condense_identity(self, messages):
        return self.gpt.chat(
            messages,
            system_prompt=IDENTITY_PROMPT
        )

