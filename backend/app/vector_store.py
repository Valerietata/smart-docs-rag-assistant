import chromadb
from backend.app.models import DocumentChunk

client = chromadb.PersistentClient(
    path="./chroma_data"
)

collection = client.get_or_create_collection(
    name="smart_docs"
)

def add_chunks(
    chunks: list[DocumentChunk],
    embeddings: list[list[float]],
    document_id: str,
) -> None:
    collection.add(
        ids=[
            f"{document_id}-{chunk.chunk_index}"
            for chunk in chunks
        ],
        documents=[
            chunk.text
            for chunk in chunks
        ],
        embeddings=embeddings,
        metadatas=[
            {
                "document_id": document_id,
                "source": chunk.source,
                "chunk_index": chunk.chunk_index,
            }
            for chunk in chunks
        ],
    )