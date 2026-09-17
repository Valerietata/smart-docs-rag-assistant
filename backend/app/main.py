from fastapi import FastAPI
from pydantic import BaseModel

from backend.app.rag import ask_question
from fastapi import FastAPI, File, UploadFile
from uuid import uuid4
from backend.app.document_loader import decode_text_content
from backend.app.chunking import create_document_chunks
from backend.app.embeddings import create_embeddings
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

@app.post("/documents")
def upload_document(
    file: UploadFile = File(...),
) -> dict:
    content = file.file.read()
    text = decode_text_content(content)
    chunks = create_document_chunks(
    text=text,
    source=file.filename,
)
    embeddings = create_embeddings(
    [chunk.text for chunk in chunks]
)
    document_id = str(uuid4())

    return {
    "document_id": document_id,
    "filename": file.filename,
    "size_bytes": len(content),
    "text_length": len(text),
    "chunk_count": len(chunks),
    "embedding_count": len(embeddings),
    "embedding_dimensions": len(embeddings[0]),
}
    