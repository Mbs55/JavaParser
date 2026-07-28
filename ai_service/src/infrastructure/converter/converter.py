from pathlib import Path
path="../../../docs"
files=Path(path).rglob("*")
for file in files:
    if file.suffix in [".md",".adoc",".txt",".html"]:
        txt=file.read_text(encoding="utf-8")