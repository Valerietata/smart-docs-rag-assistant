import json

from backend.app.retrieval import retrieve


def evaluate_retrieval(
    test_file: str,
    top_k: int = 2,
) -> dict:
    with open(test_file, "r", encoding="utf-8") as file:
        test_cases = json.load(file)

    passed = 0
    results = []

    for test_case in test_cases:
        question = test_case["question"]
        expected_chunk_index = test_case["expected_chunk_index"]

        retrieval_results = retrieve(
            question=question,
            top_k=top_k,
        )

        retrieved_metadatas = retrieval_results["metadatas"][0]

        retrieved_chunk_indexes = [
            metadata["chunk_index"]
            for metadata in retrieved_metadatas
        ]

        is_correct = expected_chunk_index in retrieved_chunk_indexes

        if is_correct:
            passed += 1

        results.append(
            {
                "question": question,
                "expected_chunk_index": expected_chunk_index,
                "retrieved_chunk_indexes": retrieved_chunk_indexes,
                "passed": is_correct,
            }
        )

    accuracy = passed / len(test_cases)

    return {
        "accuracy": accuracy,
        "passed": passed,
        "total": len(test_cases),
        "results": results,
    }