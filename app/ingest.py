import os
import uuid
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from app.embeddings import embed_text
from app.chunker import chunk_text
from app.loader import load_documents

COLLECTION = "policy_docs"

client = QdrantClient(path="qdrant_storage")


def ingest_pdf(file_path):

    filename = os.path.basename(file_path)

    # Load document text
    text = load_documents([file_path])[0]["text"]

    # Split into chunks
    chunks = chunk_text(text)

    # Create embeddings
    
    embeddings = embed_text(chunks)

    points = []

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

        point = PointStruct(
            id=str(uuid.uuid4()),
            vector=embedding.tolist(),
            payload={
                "text": chunk,
                "source": filename,   # 🔴 THIS FIXES YOUR SOURCE ISSUE
                "chunk_id": i
            }
        )

        points.append(point)

    # Insert into Qdrant
    client.upsert(
        collection_name=COLLECTION,
        points=points
    )

    print(f"Indexed {len(points)} chunks from {filename}")


def ingest_folder(folder):

    for file in os.listdir(folder):

        if file.endswith(".pdf"):

            ingest_pdf(os.path.join(folder, file))


if __name__ == "__main__":

    ingest_folder("documents")