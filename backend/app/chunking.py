from backend.app.models import DocumentChunk

def split_text(
    text: str,
    chunk_size: int = 100,
    overlap: int = 20,
) -> list[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))

        if end < len(text):
            last_space = text.rfind(" ", start, end)

            if last_space > start:
                end = last_space

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)
        if end == len(text):
            break

        next_start = max(end - overlap, start + 1)

        last_space = text.rfind(" ", start, next_start)

        if last_space > start:
            next_start = last_space + 1

        start = next_start

    return chunks

def create_document_chunks(
    text: str,
    source: str,
    chunk_size: int = 100,
    overlap: int = 20,
) -> list[DocumentChunk]:
    text_chunks = split_text(
        text=text,
        chunk_size=chunk_size,
        overlap=overlap,
    )

    document_chunks = []

    for index, chunk_text in enumerate(text_chunks):
        document_chunks.append(
            DocumentChunk(
                text=chunk_text,
                source=source,
                chunk_index=index,
            )
        )

    return document_chunks