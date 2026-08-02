import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.infrastructure.converter.converter import convert_file


class ConverterPdfTests(unittest.TestCase):
    def test_convert_file_extracts_text_from_pdf(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            source = tmp_path / "sample.pdf"
            source.write_bytes(
                b"%PDF-1.4\n"
                b"1 0 obj\n"
                b"<< /Type /Catalog /Pages 2 0 R >>\n"
                b"endobj\n"
                b"2 0 obj\n"
                b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>\n"
                b"endobj\n"
                b"3 0 obj\n"
                b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 300 144] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\n"
                b"endobj\n"
                b"4 0 obj\n"
                b"<< /Length 44 >>\n"
                b"stream\n"
                b"BT /F1 18 Tf 72 72 Td (Hello PDF) Tj ET\n"
                b"endstream\n"
                b"endobj\n"
                b"5 0 obj\n"
                b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\n"
                b"endobj\n"
                b"xref\n"
                b"0 6\n"
                b"0000000000 65535 f \n"
                b"0000000010 00000 n \n"
                b"0000000062 00000 n \n"
                b"0000000119 00000 n \n"
                b"0000000206 00000 n \n"
                b"0000000300 00000 n \n"
                b"trailer\n"
                b"<< /Root 1 0 R /Size 6 >>\n"
                b"startxref\n"
                b"0\n"
                b"%%EOF\n"
            )

            output_dir = tmp_path / "out"
            output_file = convert_file(source, output_dir)

            self.assertTrue(output_file.exists())
            content = output_file.read_text(encoding="utf-8")
            self.assertIn("Hello PDF", content)


if __name__ == "__main__":
    unittest.main()
