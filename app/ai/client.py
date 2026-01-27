from openai import OpenAI

### Gateway Pattern ###
class GPTClient:
    def __init__(self):
        self.client = OpenAI()

    def chat(self, messages, system_prompt=None):
        full_messages = []
        if system_prompt:
            full_messages.append({"role": "system", "content": system_prompt})
        full_messages.extend(messages)

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=full_messages
        )
        return response.choices[0].message.content

