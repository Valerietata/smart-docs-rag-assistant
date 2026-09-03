import json
from pathlib import Path

from backend.app.chunking import create_document_chunks
from backend.app.document_loader import load_text_file
from backend.app.generation import generate_answer
from backend.app.retrieval import retrieve

from backend.app.rag import ask_question

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
def evaluate_generation(
    test_file: str,
    document_file: str,
) -> dict:
    with open(test_file, "r", encoding="utf-8") as file:
        test_cases = json.load(file)

    text = load_text_file(document_file)

    chunks = create_document_chunks(
        text=text,
        source=Path(document_file).name,
    )

    passed = 0
    results = []

    for test_case in test_cases:
        question = test_case["question"]
        expected_answer = test_case["expected_answer"]
        expected_chunk_index = test_case["expected_chunk_index"]

        context = chunks[expected_chunk_index].text

        generated_answer = generate_answer(
            question=question,
            context=context,
        )

        is_correct = (
            expected_answer.lower()
            in generated_answer.lower()
        )

        if is_correct:
            passed += 1

        results.append(
            {
                "question": question,
                "expected_answer": expected_answer,
                "generated_answer": generated_answer,
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

def evaluate_end_to_end(
    test_file: str,
) -> dict:
    with open(test_file, "r", encoding="utf-8") as file:
        test_cases = json.load(file)

    passed = 0
    results = []

    for test_case in test_cases:
        question = test_case["question"]
        expected_answer = test_case["expected_answer"]

        rag_result = ask_question(question)

        generated_answer = rag_result["answer"]

        is_correct = (
            expected_answer.lower()
            in generated_answer.lower()
        )

        if is_correct:
            passed += 1

        results.append(
            {
                "question": question,
                "expected_answer": expected_answer,
                "generated_answer": generated_answer,
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