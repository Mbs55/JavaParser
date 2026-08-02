from __future__ import annotations

import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

from pypdf import PdfReader


class HTMLTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        if data:
            self.parts.append(data)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"p", "div", "section", "article", "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr", "ul", "ol"}:
            self.parts.append("\n")
        elif tag in {"br", "hr"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"p", "div", "section", "article", "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr", "ul", "ol"}:
            self.parts.append("\n")

    def get_text(self) -> str:
        return "".join(self.parts)


def strip_html_to_text(raw_html: str) -> str:
    parser = HTMLTextExtractor()
    parser.feed(raw_html)
    parser.close()
    return unescape(parser.get_text()).strip()


def convert_asciidoc(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            lines.append("")
            continue
        if stripped.startswith("//"):
            continue
        if stripped.startswith(":"):
            continue
        if stripped.startswith("["):
            continue
        heading_match = re.match(r"^(=+)(?:\s+)(.+)$", stripped)
        if heading_match:
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            lines.append(f"{'#' * min(level, 6)} {title}")
            continue
        bullet_match = re.match(r"^\*\s+(.+)$", stripped)
        if bullet_match:
            lines.append(f"- {bullet_match.group(1).strip()}")
            continue
        lines.append(stripped)
    return "\n".join(lines).strip()


def normalize_markdown(text: str, title: str) -> str:
    cleaned = text.strip()
    if not cleaned:
        cleaned = f"_No content extracted._"
    return f"---\nsource: {title}\n---\n\n# {title}\n\n{cleaned}\n"


def extract_pdf_text(source: Path) -> str:
    reader = PdfReader(str(source))
    pages: list[str] = []
    for page in reader.pages:
        extracted = page.extract_text() or ""
        pages.append(extracted.strip())
    return "\n\n".join(page for page in pages if page).strip()


def convert_file(source: Path, output_dir: Path) -> Path:
    relative_path = source.relative_to(base_dir)
    target_path = output_dir / relative_path
    target_path = target_path.with_suffix(".md")
    target_path.parent.mkdir(parents=True, exist_ok=True)

    text = source.read_text(encoding="utf-8", errors="ignore")
    suffix = source.suffix.lower()

    if suffix == ".md":
        content = text
    elif suffix == ".adoc":
        content = convert_asciidoc(text)
    elif suffix == ".html":
        content = strip_html_to_text(text)
    elif suffix == ".txt":
        content = text
    elif suffix == ".pdf":
        content = extract_pdf_text(source)
    else:
        raise ValueError(f"Unsupported format for {source}")

    title = source.stem.replace("_", " ").replace("-", " ")
    target_path.write_text(normalize_markdown(content, title), encoding="utf-8")
    return target_path


base_dir = Path(__file__).resolve().parents[3]
docs_dir = base_dir / "docs"
out_dir = base_dir / "rag_docs"
out_dir.mkdir(parents=True, exist_ok=True)

files = sorted(docs_dir.rglob("*"))
converted_files = []
for file in files:
    if file.is_file() and file.suffix.lower() in {".md", ".adoc", ".txt", ".html", ".pdf"}:
        converted_files.append(convert_file(file, out_dir))

index_lines = ["# RAG Documentation Index", "", f"Converted {len(converted_files)} documentation files from {docs_dir.name}.", ""]
for path in converted_files:
    rel = path.relative_to(out_dir).as_posix()
    index_lines.append(f"- [{rel}]({rel})")
(out_dir / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

print(f"Converted {len(converted_files)} documents to {out_dir}")