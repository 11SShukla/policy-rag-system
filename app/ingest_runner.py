import os
from pydoc import text
import uuid

from qdrant_client.models import VectorParams, Distance
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

from app.loader import load_documents
from app.chunker import chunk_text
from app.embeddings import embed_text
from app.supersession_detector import detect_supersession
from app.supersession_detector import detect_supersession

superseded_docs = detect_supersession(text)

COLLECTION = "policy_docs"

client = QdrantClient(path="qdrant_storage")
COLLECTION = "policy_docs"

# create collection if not exists
collections = client.get_collections().collections

if COLLECTION not in [c.name for c in collections]:

    client.create_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )

def ingest():

    data_path = "data_RBI"

    documents = load_documents(data_path)

    points = []

    for doc in documents:

        source = doc["doc_id"]
        text = doc["text"]

        print(f"Processing {source}")

        # detect supersession
        superseded_docs = detect_supersession(text)

        chunks = chunk_text(text)

        embeddings = embed_text(chunks)

        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

            payload = {
                "text": chunk,
                "source": source,
                "chunk_id": i,
                "supersedes": superseded_docs
            }

            point = PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding.tolist(),
                payload=payload
            )

            points.append(point)

    client.upsert(
        collection_name=COLLECTION,
        points=points
    )

    print(f"Indexed {len(points)} chunks successfully")


if __name__ == "__main__":
    ingest()