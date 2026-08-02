import re
from pathlib import Path


def _get_knowledge_dir() -> Path:
    current_file = Path(__file__).resolve()
    candidates = [
        current_file.parents[3] / "knowledge",
        current_file.parents[2] / "knowledge",
        current_file.parents[1] / "knowledge",
    ]

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return current_file.parents[3] / "knowledge"


def markdown_chunker(text: str, max_size: int = 1000):
    if max_size <= 0:
        raise ValueError("max_size must be greater than 0")

    chunks = []
    sections = re.split(r"(?=^#{1,6}\s)", text, flags=re.MULTILINE)

    for section in sections:
        section = section.strip()

        if not section:
            continue

        if len(section) <= max_size:
            chunks.append(section)
            continue

        start = 0
        while start < len(section):
            end = min(start + max_size, len(section))
            split_pos = section.rfind("\n\n", start, end)

            if split_pos <= start:
                split_pos = end

            chunk = section[start:split_pos].strip()
            if not chunk:
                chunk = section[start:end].strip()

            if chunk:
                chunks.append(chunk)

            start = split_pos
            if start >= len(section):
                break

    return chunks


def chunking_rag_docs():
    knowledge_dir = _get_knowledge_dir()
    chunks: list[str] = []

    for md in knowledge_dir.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        chunks.extend(markdown_chunker(text))

    return chunks
