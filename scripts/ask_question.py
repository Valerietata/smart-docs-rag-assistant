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

    answer = ask_question(args.question)

    print()
    print("QUESTION")
    print(args.question)

    print()
    print("ANSWER")
    print(answer)


if __name__ == "__main__":
    main()