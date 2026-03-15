import os
from groq import Groq
from dotenv import load_dotenv
from app.memory import get_memory

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

client = Groq(api_key=api_key)


def generate_answer(question: str, context: str) -> str:
    memory = get_memory()

    prompt = f"""
You are an expert assistant explaining government and regulatory policies.

Use ONLY the information provided in the context below.

Rules:
- Do NOT invent or assume any information.
- If the answer is not found in the context, respond with:
  "The provided documents do not contain enough information to answer this question."
- Summarize and explain rules clearly — do not copy raw text verbatim.
- Avoid repetition.
- Use bullet points for clarity and readability.
- Cite specific chunks using [Chunk X] inline where relevant.
- At the end, list all sources/chunks used under a "Sources" section.

Conversation History:
{memory if memory else "No prior conversation."}

Context:
{context}

Question:
{question}

Provide a clear, structured answer with bullet points, inline chunk citations, and a sources list at the end.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=500,
    )

    return response.choices[0].message.content