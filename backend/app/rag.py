from backend.app.generation import generate_answer
from backend.app.retrieval import retrieve


def ask_question(question: str, top_k: int = 2) -> dict:
    results = retrieve(
        question=question,
        top_k=top_k,
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    context_parts = []
    sources = []

    for index, (document, metadata) in enumerate(
        zip(documents, metadatas),
        start=1,
    ):
        label = f"S{index}"

        context_parts.append(
            f"""[{label}]
Source: {metadata["source"]}
Chunk: {metadata["chunk_index"]}
Text:
{document}"""
        )

        sources.append(
            {
                "label": f"[{label}]",
                "source": metadata["source"],
                "chunk_index": metadata["chunk_index"],
            }
        )

    context = "\n\n".join(context_parts)

    answer = generate_answer(
        question=question,
        context=context,
    )

    return {
        "answer": answer,
        "sources": sources,
    }