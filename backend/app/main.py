from fastapi import FastAPI
from pydantic import BaseModel

from backend.app.rag import ask_question

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.get("/health")
def health_check() -> dict:
    return {
        "status": "healthy"
    }

@app.post("/questions")
def ask_rag_question(request: QuestionRequest) -> dict:
    result = ask_question(request.question)

    return result