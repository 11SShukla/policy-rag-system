from qdrant_client import QdrantClient
from app.embeddings import embed_text
from app.bm25_index import load_bm25, search_bm25
import atexit


client = QdrantClient(path="qdrant_storage")
atexit.register(client.close)
load_bm25()

COLLECTION = "policy_docs"


def vector_search(query, k=10):

    vector = embed_text([query])[0].tolist()

    results = client.query_points(
        collection_name=COLLECTION,
        query=vector,
        limit=k
    )

    chunks = []

    for r in results.points:
        chunks.append({
            "text": r.payload["text"],
            "source": r.payload.get("source", "unknown"),
            "chunk_id": r.payload.get("chunk_id", 0)
        })

    return chunks


def hybrid_search(query, k=10):

    vector_results = vector_search(query, k)

    bm25_raw = search_bm25(query, k)

    bm25_results = []

    for r in bm25_raw:
        bm25_results.append({
            "text": r[0],
            "source": r[1] if len(r) > 1 else "unknown"
        })

    combined = vector_results + bm25_results

    seen = set()
    unique = []

    for c in combined:
        if c["text"] not in seen:
            seen.add(c["text"])
            unique.append(c)

    return unique[:8]