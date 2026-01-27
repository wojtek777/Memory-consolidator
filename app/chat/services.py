from app.ai.client import GPTClient

class ChatService:
    def __init__(self):
        self.gpt = GPTClient()

    def reply(self, messages):
        """
        messages: list of dicts [{role, content}]
        """
        return self.gpt.chat(messages)

