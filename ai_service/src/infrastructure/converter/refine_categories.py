from __future__ import annotations

import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
KNOWLEDGE_DIR = BASE_DIR / "knowledge"

CATEGORY_RULES = {
    "ai-llm-security": [
        "ai_agent",
        "llm",
        "mcp",
        "rag",
        "secure_ai",
        "secure_coding_with_ai",
    ],
    "cloud-devops-security": [
        "docker",
        "kubernetes",
        "ci_cd",
        "infrastructure_as_code",
        "secure_cloud_architecture",
        "serverless",
        "nodejs_docker",
    ],
    "browser-mobile-security": [
        "browser_extension",
        "mobile_application",
        "html5",
        "xs_leaks",
        "third_party_javascript",
        "websocket",
    ],
}


def normalize(name: str) -> str:
    return name.lower().replace(" ", "_").replace("-", "_")


def move_files() -> list[str]:
    moved: list[str] = []
    for category, patterns in CATEGORY_RULES.items():
        destination = KNOWLEDGE_DIR / category
        destination.mkdir(parents=True, exist_ok=True)
        for source_file in sorted(KNOWLEDGE_DIR.rglob("*.md")):
            if not source_file.is_file():
                continue
            stem = normalize(source_file.stem)
            if any(pattern in stem for pattern in patterns):
                target = destination / source_file.name
                if source_file != target:
                    shutil.move(str(source_file), str(target))
                    moved.append(f"{source_file.relative_to(KNOWLEDGE_DIR)} -> {category}/{source_file.name}")
    return moved


if __name__ == "__main__":
    moved = move_files()
    print(f"Moved {len(moved)} files into new categories")
    for item in moved:
        print(item)
