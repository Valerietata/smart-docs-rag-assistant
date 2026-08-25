from backend.app.embeddings import create_embedding
from backend.app.vector_store import collection


def retrieve(question: str, top_k: int = 2):
    question_embedding = create_embedding(question)

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )

    return results