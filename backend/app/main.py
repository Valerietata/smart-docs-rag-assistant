from fastapi import FastAPI
from pydantic import BaseModel

from backend.app.rag import ask_question

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str
class SourceResponse(BaseModel):
    label: str
    source: str
    chunk_index: int
class QuestionResponse(BaseModel):
    answer: str
    sources: list[SourceResponse]
@app.get("/health")
def health_check() -> dict:
    return {
        "status": "healthy"
    }

@app.post(
    "/questions",
    response_model=QuestionResponse,
)
def ask_rag_question(request: QuestionRequest,) -> QuestionResponse:
    result = ask_question(request.question)
    return QuestionResponse(**result)