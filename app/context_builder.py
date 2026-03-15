def build_context(chunks):

    context_parts = []

    for i, c in enumerate(chunks, start=1):

        text = c["text"]
        source = c.get("source", "unknown")

        context_parts.append(
            f"[Chunk {i} | Source: {source}]\n{text}"
        )

    return "\n\n".join(context_parts)