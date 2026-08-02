import subprocess
import sys
import textwrap
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ChunkingServiceTests(unittest.TestCase):
    def test_markdown_chunker_does_not_loop_on_repeated_split_points(self) -> None:
        code = textwrap.dedent(
            f"""
            import sys
            sys.path.insert(0, r\"{ROOT}\")
            from src.infrastructure.chunking.chunkingService import markdown_chunker

            text = \"x\\n\\n\" + \"y\" * 20
            chunks = markdown_chunker(text, max_size=10)
            print(len(chunks))
            """
        )

        completed = subprocess.run(
            [sys.executable, "-c", code],
            capture_output=True,
            text=True,
            timeout=5,
            check=True,
        )

        self.assertTrue(completed.stdout.strip())


if __name__ == "__main__":
    unittest.main()
