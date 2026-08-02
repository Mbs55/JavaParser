from __future__ import annotations

import shutil
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[3]
SOURCE_DIR = BASE_DIR / "rag_docs" / "docs"
TARGET_ROOT = BASE_DIR / "rag_docs" / "chunks"

CATEGORY_RULES = [
    (
        "sql-injection",
        [
            "sql injection",
            "sql-injection",
            "sql_injection",
            "query parameterization",
            "ldap injection",
            "os command injection",
            "injection prevention",
        ],
    ),
    (
        "cross-site-scripting",
        [
            "cross site scripting",
            "cross-site-scripting",
            "xss",
            "dom clobbering",
            "dom_based",
            "clickjacking",
            "content security policy",
            "xs leaks",
        ],
    ),
    (
        "jdbc-and-database",
        [
            "jdbc",
            "database security",
            "database",
            "query parameterization",
            "session management",
        ],
    ),
    (
        "spring-security-migration",
        [
            "migration",
            "spring security",
            "springsec",
            "spring-security",
            "servlet",
            "reactive",
        ],
    ),
    (
        "authentication-and-authorization",
        [
            "authentication",
            "authorization",
            "oauth",
            "openid",
            "mfa",
            "access control",
            "role",
            "policy",
            "forgot password",
            "passkeys",
        ],
    ),
    (
        "web-application-security",
        [
            "rest security",
            "http headers",
            "csrf",
            "cors",
            "cookies",
            "input validation",
            "websocket",
            "http",
        ],
    ),
    (
        "java-security",
        [
            "java security",
            "secure coding",
            "cert",
            "oracle",
            "jaas",
            "deserialization",
            "java",
        ],
    ),
    (
        "cryptography-and-secrets",
        [
            "crypto",
            "cryptographic",
            "key management",
            "secret",
            "tls",
            "jwt",
            "password storage",
        ],
    ),
    (
        "cloud-devops-and-infrastructure",
        [
            "docker",
            "kubernetes",
            "infrastructure as code",
            "cloud",
            "ci_cd",
            "devops",
            "serverless",
            "container",
        ],
    ),
    (
        "ai-agent-and-llm-security",
        [
            "ai agent",
            "llm",
            "prompt injection",
            "mcp",
            "secure ai",
            "rag security",
        ],
    ),
    (
        "cwe-owasp",
        [
            "cwe",
            "owasp",
            "top10",
            "top25",
            "threat modeling",
            "vulnerability disclosure",
        ],
    ),
    (
        "supply-chain-and-dependencies",
        [
            "software supply chain",
            "sbom",
            "dependency",
            "package",
            "npm",
            "composer",
            "php",
            "nodejs",
        ],
    ),
    (
        "browser-and-mobile-security",
        [
            "browser extension",
            "mobile application",
            "browser",
            "mobile",
        ],
    ),
]


def normalize_text(value: str) -> str:
    return value.lower().replace("_", " ").replace("-", " ")


def classify(path: Path) -> str:
    text = normalize_text(path.as_posix())
    for category, keywords in CATEGORY_RULES:
        if any(keyword in text for keyword in keywords):
            return category
    return "general-security"


def copy_markdown_files() -> list[tuple[str, Path]]:
    TARGET_ROOT.mkdir(parents=True, exist_ok=True)
    copied: list[tuple[str, Path]] = []
    for source_file in sorted(SOURCE_DIR.rglob("*.md")):
        if not source_file.is_file():
            continue
        category = classify(source_file)
        destination_dir = TARGET_ROOT / category
        destination_dir.mkdir(parents=True, exist_ok=True)
        relative_path = source_file.relative_to(SOURCE_DIR)
        destination_file = destination_dir / relative_path
        destination_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, destination_file)
        copied.append((category, destination_file))
    return copied


def write_index(copied: list[tuple[str, Path]]) -> None:
    counts: dict[str, int] = {}
    for category, _ in copied:
        counts[category] = counts.get(category, 0) + 1

    lines = [
        "# RAG Chunk Index",
        "",
        "This folder groups the generated Markdown documents into topic-based chunks for retrieval.",
        "",
    ]
    for category in sorted(counts):
        lines.append(f"- [{category}]({category}/)")
        lines.append(f"  - Files: {counts[category]}")

    (TARGET_ROOT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    copied = copy_markdown_files()
    write_index(copied)
    print(f"Organized {len(copied)} markdown files into {TARGET_ROOT}")
