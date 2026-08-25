import argparse

from backend.app.retrieval import retrieve

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Search the vector database for relevant document chunks."
    )

    parser.add_argument(
        "question",
        help="Question to search for.",
    )

    parser.add_argument(
        "--top-k",
        type=int,
        default=2,
        help="Number of chunks to retrieve.",
    )

    args = parser.parse_args()

    results = retrieve(
        question=args.question,
        top_k=args.top_k,
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    print()
    print("=" * 70)
    print("RAG RETRIEVAL RESULTS")
    print("=" * 70)
    print(f"Question: {args.question}")
    print()

    for index, (document, metadata, distance) in enumerate(
        zip(documents, metadatas, distances),
        start=1,
    ):
        print(f"RESULT {index}")
        print(f"Source:      {metadata['source']}")
        print(f"Chunk index: {metadata['chunk_index']}")
        print(f"Distance:    {distance:.4f}")
        print()
        print(document)
        print()
        print("-" * 70)


if __name__ == "__main__":
    main()