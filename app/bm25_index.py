from rank_bm25 import BM25Okapi
import pickle

bm25 = None
documents = []

def build_bm25(chunks):
    global bm25, documents

    documents = chunks
    tokenized = [doc.split() for doc in documents]

    bm25 = BM25Okapi(tokenized)

    with open("bm25_index.pkl", "wb") as f:
        pickle.dump((bm25, documents), f)

def load_bm25():
    global bm25, documents

    with open("bm25_index.pkl", "rb") as f:
        bm25, documents = pickle.load(f)

def search_bm25(query, k=5):
    tokens = query.split()
    scores = bm25.get_scores(tokens)

    ranked = sorted(
        list(zip(documents, scores)),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:k]