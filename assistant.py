# assistant.py

from openai import OpenAI
from config import PERPLEXITY_API_KEY, PERPLEXITY_MODEL

def ask_perplexity(question):
    client = OpenAI(
        api_key=PERPLEXITY_API_KEY,
        base_url="https://api.perplexity.ai"
    )
    response = client.chat.completions.create(
        model=PERPLEXITY_MODEL,
        messages=[
            {"role": "system", "content": "Tu es un assistant utile et concis."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content
