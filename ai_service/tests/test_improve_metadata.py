import json
import tempfile
from pathlib import Path

from src.infrastructure.converter import improve_metadata


def test_main_skips_empty_records(tmp_path: Path) -> None:
    input_path = tmp_path / "rag_chunks.jsonl"
    output_path = tmp_path / "rag_chunks_enriched.jsonl"

    input_path.write_text(
        "{}\n"
        '{"id": "1", "title": "SQL Injection", "text": "PreparedStatement and SQL injection prevention."}\n',
        encoding="utf-8",
    )

    improve_metadata.INPUT_FILE = input_path
    improve_metadata.OUTPUT_FILE = output_path

    improve_metadata.main()

    written = [json.loads(line) for line in output_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(written) == 1
    assert written[0]["id"] == "1"
    assert written[0]["category"] == "Database"
