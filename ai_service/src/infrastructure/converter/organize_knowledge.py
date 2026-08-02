from __future__ import annotations

import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
SOURCE_DIR = BASE_DIR / "rag_docs" / "docs"
TARGET_ROOT = BASE_DIR / "knowledge"

CATEGORY_MAP = {
    "authentication": [
        "authentication", "login", "password", "mfa", "remember me", "session", "identity", "passkeys", "forgot password"
    ],
    "authorization": [
        "authorization", "access control", "permission", "role", "acl", "method security"
    ],
    "spring-security": [
        "spring security", "springsec", "spring-security", "security filter", "filter", "csrf", "cors", "header", "oauth2", "jwt", "password encoding", "configuration", "migration", "websecurityconfigureradapter"
    ],
    "injection": [
        "sql injection", "sql", "command injection", "ldap injection", "xpath", "nosql", "expression language", "xxe", "injection"
    ],
    "web-security": [
        "xss", "clickjacking", "csrf", "cors", "cookie", "header", "file upload", "redirect", "http headers"
    ],
    "database": [
        "jdbc", "prepared statement", "transactions", "connection pooling", "hibernate", "jpa", "database security"
    ],
    "cryptography": [
        "cryptography", "hash", "encryption", "signature", "key", "random", "certificate", "tls", "jwt"
    ],
    "serialization": [
        "serialization", "deserialization", "jackson", "json", "xml"
    ],
    "java": [
        "reflection", "process execution", "filesystem", "classloading", "concurrency", "exception", "logging", "networking", "io"
    ],
    "input-validation": [
        "input validation", "validation", "canonicalization", "sanitization", "encoding"
    ],
    "secrets": [
        "secret", "credential", "api key", "configuration"
    ],
    "dependency-security": [
        "dependency", "sbom", "package", "npm", "composer", "software supply chain"
    ],
    "secure-design": [
        "threat modeling", "secure design", "business logic", "zero trust", "secure product design"
    ],
    "secure-coding": [
        "secure coding", "secure code review", "code review", "coding"
    ],
    "vulnerabilities": [
        "vulnerabilities", "vulnerability", "weakness", "attack surface"
    ],
    "cwe": [
        "cwe", "owasp top 10", "top 25"
    ],
}

SUBCATEGORY_RULES = {
    "authentication": [
        ("passwords", ["password", "password storage"]),
        ("mfa", ["mfa", "multifactor"]),
        ("session", ["session"]),
        ("remember-me", ["remember me"]),
        ("login", ["login"]),
        ("identity", ["identity"]),
    ],
    "authorization": [
        ("roles", ["role"]),
        ("permissions", ["permission", "access control"]),
        ("acl", ["acl"]),
        ("method-security", ["method security"]),
    ],
    "spring-security": [
        ("authentication", ["authentication"]),
        ("authorization", ["authorization"]),
        ("csrf", ["csrf"]),
        ("cors", ["cors"]),
        ("headers", ["header"]),
        ("filters", ["filter"]),
        ("oauth2", ["oauth2", "oauth"]),
        ("jwt", ["jwt"]),
        ("sessions", ["session"]),
        ("password-encoding", ["password encoding"]),
        ("configuration", ["configuration", "websecurityconfigureradapter"]),
        ("migration", ["migration"]),
    ],
    "injection": [
        ("sql", ["sql injection", "sql"]),
        ("command", ["command injection"]),
        ("ldap", ["ldap"]),
        ("xpath", ["xpath"]),
        ("nosql", ["nosql"]),
        ("expression-language", ["expression language"]),
        ("xxe", ["xxe"]),
    ],
    "web-security": [
        ("csrf", ["csrf"]),
        ("xss", ["xss"]),
        ("clickjacking", ["clickjacking"]),
        ("cors", ["cors"]),
        ("cookies", ["cookie"]),
        ("headers", ["header"]),
        ("file-upload", ["file upload"]),
        ("redirects", ["redirect"]),
    ],
    "database": [
        ("jdbc", ["jdbc"]),
        ("prepared-statements", ["prepared statement"]),
        ("transactions", ["transaction"]),
        ("connection-pooling", ["connection pooling"]),
        ("hibernate", ["hibernate"]),
        ("jpa", ["jpa"]),
    ],
    "cryptography": [
        ("hashing", ["hash"]),
        ("encryption", ["encryption"]),
        ("signatures", ["signature"]),
        ("keys", ["key"]),
        ("random", ["random"]),
        ("certificates", ["certificate"]),
        ("tls", ["tls"]),
    ],
    "serialization": [
        ("java-serialization", ["serialization"]),
        ("deserialization", ["deserialization"]),
        ("jackson", ["jackson"]),
        ("json", ["json"]),
        ("xml", ["xml"]),
    ],
    "java": [
        ("reflection", ["reflection"]),
        ("process-execution", ["process execution"]),
        ("filesystem", ["filesystem", "file handling"]),
        ("classloading", ["classloading"]),
        ("concurrency", ["concurrency"]),
        ("exceptions", ["exception"]),
        ("logging", ["logging"]),
        ("networking", ["networking"]),
        ("io", ["io"]),
    ],
    "input-validation": [
        ("validation", ["validation"]),
        ("canonicalization", ["canonicalization"]),
        ("sanitization", ["sanitization"]),
        ("encoding", ["encoding"]),
    ],
    "secrets": [
        ("credentials", ["credential"]),
        ("api-keys", ["api key"]),
        ("configuration", ["configuration"]),
    ],
}


def normalize(text: str) -> str:
    return text.lower().replace("_", " ").replace("-", " ")


def classify(path: Path) -> tuple[str, str]:
    text = normalize(path.as_posix())
    for category, keywords in CATEGORY_MAP.items():
        if any(keyword in text for keyword in keywords):
            subcategory = ""
            if category in SUBCATEGORY_RULES:
                for candidate, terms in SUBCATEGORY_RULES[category]:
                    if any(term in text for term in terms):
                        subcategory = candidate
                        break
            return category, subcategory
    return "secure-coding", ""


def move_markdown_files() -> list[tuple[str, str, Path]]:
    if TARGET_ROOT.exists():
        shutil.rmtree(TARGET_ROOT)
    TARGET_ROOT.mkdir(parents=True, exist_ok=True)

    moved: list[tuple[str, str, Path]] = []
    for source_file in sorted(SOURCE_DIR.rglob("*.md")):
        if not source_file.is_file():
            continue
        category, subcategory = classify(source_file)
        destination_dir = TARGET_ROOT / category
        if subcategory:
            destination_dir = destination_dir / subcategory
        destination_dir.mkdir(parents=True, exist_ok=True)
        relative_path = source_file.relative_to(SOURCE_DIR)
        destination_file = destination_dir / relative_path.name
        shutil.move(str(source_file), str(destination_file))
        moved.append((category, subcategory, destination_file))
    return moved


def write_index(copied: list[tuple[str, str, Path]]) -> None:
    counts: dict[str, int] = {}
    for category, subcategory, _ in copied:
        counts[(category, subcategory)] = counts.get((category, subcategory), 0) + 1

    lines = [
        "# Knowledge Base Index",
        "",
        "This structure is organized by security concepts for Java SAST RAG retrieval.",
        "",
    ]
    for (category, subcategory), count in sorted(counts.items()):
        label = category if not subcategory else f"{category}/{subcategory}"
        lines.append(f"- [{label}]({label}/)")
        lines.append(f"  - Files: {count}")

    (TARGET_ROOT / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    moved = move_markdown_files()
    write_index(moved)
    print(f"Organized {len(moved)} markdown files into {TARGET_ROOT}")
