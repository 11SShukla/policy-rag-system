from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def expand_query(question):

    prompt = f"""
Generate 3 alternative search queries for retrieving policy documents.

Original query:
{question}

Return only the queries separated by newline.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    queries = response.choices[0].message.content.split("\n")

    queries.append(question)

    return list(set(q.strip() for q in queries if q.strip()))