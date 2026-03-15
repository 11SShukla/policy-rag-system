import uuid
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

client = QdrantClient(path="qdrant_storage")

COLLECTION_NAME = "policy_docs"


def init_collection():

    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )


def store_chunks(chunks, embeddings, doc_id):

    points = []

    for i, chunk in enumerate(chunks):

        point = PointStruct(
            id=str(uuid.uuid4()),   # THIS IS THE FIX
            vector=embeddings[i].tolist(),
            payload={
                "text": chunk,
                "source": doc_id,
                "chunk_id": i
            }
        )

        points.append(point)

    print(f"Storing {len(points)} chunks from {doc_id}")

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )