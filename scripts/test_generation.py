from backend.app.generation import generate_answer


question = "How much annual leave do I get?"

context = """
Employees receive 20 days of annual leave each year.
"""

answer = generate_answer(
    question=question,
    context=context,
)

print()
print("QUESTION")
print(question)

print()
print("CONTEXT")
print(context.strip())

print()
print("ANSWER")
print(answer)