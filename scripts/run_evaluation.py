from backend.app.evaluation import evaluate_retrieval


def main() -> None:
    result = evaluate_retrieval(
        test_file="data/test_questions.json",
        top_k=2,
    )

    print()
    print("RETRIEVAL EVALUATION")
    print("=" * 50)
    print(
        f'Accuracy: {result["passed"]}/{result["total"]} '
        f'({result["accuracy"]:.0%})'
    )

    print()

    for item in result["results"]:
        status = "PASS" if item["passed"] else "FAIL"

        print(f'{status} - {item["question"]}')
        print(
            f'Expected chunk: {item["expected_chunk_index"]}'
        )
        print(
            f'Retrieved chunks: {item["retrieved_chunk_indexes"]}'
        )
        print("-" * 50)


if __name__ == "__main__":
    main()
    