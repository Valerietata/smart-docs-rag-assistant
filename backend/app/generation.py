from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()


def generate_answer(question: str, context: str) -> str:
    prompt = f"""
        Answer the question using only the provided context.

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