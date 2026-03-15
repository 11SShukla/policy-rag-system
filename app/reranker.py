from sentence_transformers import CrossEncoder

# Load once at startup
model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank(query, chunks, top_k=4):

    pairs = []

    for c in chunks:
        pairs.append((query, c["text"]))

    scores = model.predict(pairs)

    ranked = sorted(
        zip(scores, chunks),
        key=lambda x: x[0],
        reverse=True
    )

    reranked_chunks = [c for score, c in ranked]

    return reranked_chunks[:top_k]