from backend.app.generation import generate_answer
from backend.app.retrieval import retrieve


def ask_question(question: str, top_k: int = 2) -> str:
    results = retrieve(
        question=question,
        top_k=top_k,
    )

    documents = results["documents"][0]

    context = "\n\n".join(documents)

    answer = generate_answer(
        question=question,
        context=context,
    )

    return answer