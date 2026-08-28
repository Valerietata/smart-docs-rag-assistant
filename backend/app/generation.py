from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()


def generate_answer(question: str, context: str) -> str:
    prompt = f"""
Answer the question using only the provided context.

Rules:
1. Do not use information that is not in the context.
2. Cite the supporting source using labels like [S1], [S2].
3. If the context does not contain enough information, say:
   "The provided documents do not contain enough information."

Question:
{question}

Context:
{context}
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt,
    )

    return response.output_text