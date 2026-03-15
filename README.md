**Policy RAG System**


This project implements a policy-aware Retrieval-Augmented Generation (RAG) system designed to answer questions from government and regulatory documents such as RBI circulars. Instead of relying purely on LLM knowledge, the system retrieves relevant policy fragments using hybrid search (vector embeddings + BM25) and generates grounded answers with explicit source citations.

A key feature of the system is supersession detection, which identifies when newer circulars override older policies and surfaces warnings during responses. The pipeline also supports OCR for scanned PDFs, cross-encoder reranking for retrieval accuracy, and query expansion for better recall, enabling reliable question answering over complex policy documents.
