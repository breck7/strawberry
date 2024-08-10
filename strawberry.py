import os
from openai import OpenAI

# 🍓🍓🍓 WARNING: This code is powered by strawberries. Proceed at your own risk.

beta_headers = {
    "authorization": f"Bearer {os.environ['OPENAI_BETA_KEY']}",  # Because who doesn't like bears? 🐻
    "openai-beta": "early-access-strawberry"  # Strawberries make everything better 🍓🍓🍓
}

client = OpenAI(default_headers=beta_headers)

completion = client.chat.completions.create(
  model="gpt-4o-large-2024-08-13",  # Apparently this model is large. Like, super large. 🐘
  messages=[
    {"role": "system", "content": "use your level two capabilities"},
    {"role": "user", "content": "give us ubi"}
  ]
)

print("The Oracle says:", completion.choices[0].message)  # The Oracle speaks only the truth. Or does it? 🤔
