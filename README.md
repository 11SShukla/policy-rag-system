Policy RAG System

An AI-powered Retrieval-Augmented Generation (RAG) system designed to answer questions from government policy documents and RBI circulars using hybrid search, reranking, and structured metadata.

The system retrieves relevant policy fragments from documents and generates accurate answers with citations and supersession warnings.

Features

Hybrid Retrieval (Vector Search + BM25)

Cross-Encoder Reranking

Query Expansion

OCR support for scanned PDFs

Supersession detection between circulars

Source citation with document names

Session memory for conversational queries

System Architecture

Pipeline:

User Query
    │
Query Expansion
    │
Hybrid Retrieval
(Vector Search + BM25)
    │
Cross Encoder Reranker
    │
Top Document Chunks
    │
Context Builder
    │
LLM Generation
    │
Answer + Sources + Supersession Warning
Tech Stack

Python

Qdrant (Vector Database)

Sentence Transformers

BM25 Retrieval

Cross Encoder Reranking

OCR (Tesseract)

Transformers / LLM APIs

Project Structure
app/

api.py
chatbot.py
chunker.py
context_builder.py
embeddings.py
ingest_runner.py
loader.py
query_expander.py
rag_pipeline.py
reference_extractor.py
reranker.py
retriever.py
supersession_detector.py
vector_store.py
Installation

Clone the repository

git clone https://github.com/11SShukla/policy-rag-system.git
cd policy-rag-system

Install dependencies

pip install -r requirements.txt
Add Documents

Place government policy PDFs inside:

data_RBI/
Ingest Documents

Run ingestion pipeline:

python -m app.ingest_runner

This will:

load PDFs

apply OCR if needed

chunk documents

generate embeddings

store vectors in Qdrant

detect supersession relationships

Run Chatbot
python -m app.chatbot

Example query:

What are RBI KYC requirements?
Example Output
Answer:
Banks must verify the identity of customers using officially valid documents
such as Aadhaar, Passport, PAN card, or Voter ID.

Sources:
KYC1.pdf
KYC5.pdf
Payment_Wallets3.pdf
Supersession Detection

The system detects when a circular replaces an earlier policy.

Example:

WARNING:
This circular supersedes earlier RBI guidelines on digital lending.
Future Improvements

Graph-based policy relationships

Retrieval evaluation metrics

Policy number extraction

Web UI interface

Knowledge graph integration
