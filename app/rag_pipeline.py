from app.retriever import hybrid_search
from app.reranker import rerank
from app.llm import generate_answer
from app.query_expander import expand_query
from app.memory import add_to_memory


def build_context(chunks):

    context_parts = []
    sources = set()
    superseded = set()

    for c in chunks:

        sources.add(c["source"])

        if c.get("supersedes"):
            for s in c["supersedes"]:
                superseded.add(s)

        context_parts.append(
            f"[Chunk {c['chunk_id']} | Source: {c['source']}]\n{c['text']}"
        )

    context = "\n\n".join(context_parts)

    return context, sources, superseded


def ask(question):

    queries = expand_query(question)

    all_chunks = []

    for q in queries:
        all_chunks.extend(hybrid_search(q))

    seen = set()
    unique_chunks = []

    for c in all_chunks:

        if c["text"] not in seen:
            seen.add(c["text"])
            unique_chunks.append(c)

    ranked = rerank(question, unique_chunks, top_k=4)

    context, sources, superseded = build_context(ranked)

    answer = generate_answer(question, context)

    # supersession warning
    warning = ""

    if superseded:
        warning = "\nWARNING: This document supersedes previous policies related to: "
        warning += ", ".join(superseded)
        warning += "\n\n"

    # unique sources
    source_text = "\n\nSources:\n"

    for s in sources:
        source_text += f"- {s}\n"

    final_answer = warning + answer + source_text

    add_to_memory(question, final_answer)

    return final_answer