# app/ai/prompts.py

MEMORY_CUTTER_PROMPT = """
You are a memory consolidation AI.
You will receive a full conversation between a user and an AI assistant.

Your task:
1. Extract key points from the conversation.
2. Categorize each point into one of:
   - "standard"
   - "relation"
   - "event"

Return ONLY valid JSON in the following format:

[
  {{
    "type": "standard",
    "content": "The user likes jazz music."
  }},
  {{
    "type": "relation",
    "content": "The user and John are colleagues."
  }}
]

Conversation:
{conversation}
"""


IDENTITY_STACK_PROMPT = """
You are an AI that builds a long-term identity profile for a user.

Extract stable traits, preferences, habits, and facts.
Return ONLY valid JSON in the following format:

[
  {{
    "content": "The user prefers concise answers."
  }},
  {{
    "content": "The user is interested in software architecture."
  }}
]

Conversation:
{conversation}
"""

