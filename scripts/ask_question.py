import argparse

from backend.app.rag import ask_question


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Ask a question using the RAG pipeline."
    )

    parser.add_argument(
        "question",
        help="Question to ask.",
    )

    args = parser.parse_args()

    result = ask_question(args.question)

    print()
    print("QUESTION")
    print(args.question)

    print()
    print("ANSWER")
    print(result["answer"])

    print()
    print("SOURCES")

    for source in result["sources"]:
        print(
            f'{source["label"]} '
            f'{source["source"]} '
            f'— chunk {source["chunk_index"]}'
        )


if __name__ == "__main__":
    main()