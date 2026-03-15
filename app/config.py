import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

QDRANT_COLLECTION = "policy_docs"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100