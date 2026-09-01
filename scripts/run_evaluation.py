from backend.app.evaluation import (
    evaluate_generation,
    evaluate_retrieval,
)


def main() -> None:
    retrieval_result = evaluate_retrieval(
        test_file="data/test_questions.json",
        top_k=2,
    )

    print()
    print("RETRIEVAL EVALUATION")
    print("=" * 50)
    print(
        f'Accuracy: {retrieval_result["passed"]}/'
        f'{retrieval_result["total"]} '
        f'({retrieval_result["accuracy"]:.0%})'
    )

    print()

    for item in retrieval_result["results"]:
        status = "PASS" if item["passed"] else "FAIL"

        print(f'{status} - {item["question"]}')
        print(
            f'Expected chunk: {item["expected_chunk_index"]}'
        )
        print(
            f'Retrieved chunks: {item["retrieved_chunk_indexes"]}'
        )
        print("-" * 50)

    generation_result = evaluate_generation(
        test_file="data/test_questions.json",
        document_file="data/sample_docs/company_policy.txt",
    )

    print()
    print("GENERATION EVALUATION")
    print("=" * 50)
    print(
        f'Accuracy: {generation_result["passed"]}/'
        f'{generation_result["total"]} '
        f'({generation_result["accuracy"]:.0%})'
    )

    print()

    for item in generation_result["results"]:
        status = "PASS" if item["passed"] else "FAIL"

        print(f'{status} - {item["question"]}')
        print(f'Expected: {item["expected_answer"]}')
        print(f'Generated: {item["generated_answer"]}')
        print("-" * 50)


if __name__ == "__main__":
    main()