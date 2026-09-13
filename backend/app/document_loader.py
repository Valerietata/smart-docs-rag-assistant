from pathlib import Path


def decode_text_content(content: bytes) -> str:
    return content.decode("utf-8")


def load_text_file(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    content = path.read_bytes()
    return decode_text_content(content)