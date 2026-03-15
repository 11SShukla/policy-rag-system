from qdrant_client import QdrantClient
from app.embeddings import embed_text

# connect to local vector DB
client = QdrantClient(path="qdrant_storage")

query = "What are RBI KYC requirements?"

# create embedding
vector = embed_text([query])[0].tolist()

# correct retrieval method
results = client.query_points(
    collection_name="policy_docs",
    query=vector,
    limit=5
)

print("\nTop Results:\n")

for r in results.points:
    print("Score:", r.score)
    print(r.payload["text"][:400])
    print("Source:", r.payload["source"])
    print("-----------\n")

client.close()