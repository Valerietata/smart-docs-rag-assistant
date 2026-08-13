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