from __future__ import annotations

import json
import re
import uuid
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parents[3]
SOURCE_ROOT = BASE_DIR / "knowledge"
OUTPUT_FILE = BASE_DIR / "rag_chunks.jsonl"

CATEGORY_MAP = {
    "authentication": "Authentication",
    "authorization": "Authorization",
    "injection": "Injection",
    "spring-security": "Spring Security",
    "database": "Database",
    "cryptography": "Cryptography",
    "serialization": "Serialization",
    "secrets": "Secrets",
    "java": "Java",
    "dependency-security": "Dependency Security",
    "secure-coding": "Secure Coding",
    "secure-design": "Secure Design",
    "web-security": "Web Security",
    "browser-mobile-security": "Browser Security",
    "cloud-devops-security": "Cloud Security",
    "ai-llm-security": "AI Security",
    "cwe": "Secure Coding",
    "vulnerabilities": "Secure Coding",
}

SOURCE_HINTS = {
    "owasp": "OWASP",
    "spring": "Spring Security",
    "cert": "CERT",
    "oracle": "Oracle",
    "findsecbugs": "FindSecBugs",
    "jdbc": "JDBC",
    "cryptography": "Oracle",
    "cwe": "CWE",
}

FRAMEWORK_HINTS = {
    "spring security": "Spring Security",
    "spring boot": "Spring Boot",
    "hibernate": "Hibernate",
    "jpa": "JPA",
    "jdbc": "JDBC",
    "servlet": "Servlet",
    "jackson": "Jackson",
    "jwt": "JWT",
    "oauth2": "OAuth2",
    "bcrypt": "BCrypt",
}

API_HINTS = [
    "PreparedStatement",
    "Statement",
    "CallableStatement",
    "Runtime.exec",
    "MessageDigest",
    "Cipher",
    "BCryptPasswordEncoder",
    "PasswordEncoder",
    "Files.readString",
    "ObjectInputStream",
    "SecurityContextHolder",
    "AuthenticationManager",
    "JdbcTemplate",
    "HttpSecurity",
    "WebSecurityConfigurerAdapter",
    "AuthenticationProvider",
    "UserDetailsService",
]

VULN_HINTS = {
    "sql injection": "SQL Injection",
    "xss": "XSS",
    "csrf": "CSRF",
    "command injection": "Command Injection",
    "ldap injection": "LDAP Injection",
    "xxe": "XXE",
    "path traversal": "Path Traversal",
    "weak cryptography": "Weak Cryptography",
    "hardcoded secret": "Hardcoded Secret",
    "unsafe deserialization": "Unsafe Deserialization",
    "ssrf": "SSRF",
    "broken authentication": "Broken Authentication",
    "broken access control": "Broken Access Control",
    "insecure deserialization": "Unsafe Deserialization",
    "deserialization": "Unsafe Deserialization",
}

CWE_PATTERN = re.compile(r"CWE[- ]?\d+", re.IGNORECASE)
OWASP_PATTERN = re.compile(r"A0\d:2021|A0\d:2017|OWASP Top 10", re.IGNORECASE)
IMPORT_PATTERN = re.compile(r"^import\s+([\w\.]+)", re.MULTILINE)
CLASS_PATTERN = re.compile(r"\b([A-Z][A-Za-z0-9_]+)\b")
ANNOTATION_PATTERN = re.compile(r"@([A-Za-z0-9_]+)")
METHOD_PATTERN = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")


def normalize_text(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\r\n?", "\n", text)
    return text.strip()


def infer_category(path: Path) -> str:
    rel = path.as_posix().lower()
    for key, value in CATEGORY_MAP.items():
        if key in rel:
            return value
    return "Secure Coding"


def infer_subcategory(path: Path, text: str) -> str:
    rel = path.as_posix().lower()
    text_l = text.lower()
    if "sql" in rel or "sql" in text_l:
        return "SQL Injection"
    if "prepared" in rel or "prepared" in text_l:
        return "Prepared Statements"
    if "password" in rel or "password" in text_l:
        return "Password Storage"
    if "oauth" in rel or "oauth" in text_l:
        return "OAuth2"
    if "jwt" in rel or "jwt" in text_l:
        return "JWT"
    if "method" in rel or "method" in text_l:
        return "Method Security"
    if "reflection" in rel or "reflection" in text_l:
        return "Reflection"
    if "file upload" in rel or "file upload" in text_l:
        return "File Upload"
    if "deserial" in rel or "deserial" in text_l:
        return "Deserialization"
    if "random" in rel or "random" in text_l:
        return "Randomness"
    if "tls" in rel or "tls" in text_l:
        return "TLS"
    if "csrf" in rel or "csrf" in text_l:
        return "CSRF"
    if "xss" in rel or "xss" in text_l:
        return "XSS"
    if "jdbc" in rel or "jdbc" in text_l:
        return "JDBC"
    if "migration" in rel or "migration" in text_l:
        return "Migration"
    if "authentication" in rel or "authentication" in text_l:
        return "Authentication"
    if "authorization" in rel or "authorization" in text_l:
        return "Authorization"
    return "General"


def infer_source(path: Path, text: str) -> str:
    text_l = text.lower()
    for key, value in SOURCE_HINTS.items():
        if key in path.as_posix().lower() or key in text_l:
            return value
    if "spring" in text_l:
        return "Spring Security"
    if "owasp" in text_l:
        return "OWASP"
    if "cwe" in text_l:
        return "CWE"
    return "OWASP"


def infer_language(text: str) -> list[str]:
    langs: list[str] = []
    lower = text.lower()
    if "```java" in text or "java" in lower or "preparedstatement" in lower:
        langs.append("Java")
    if "```sql" in text or "select" in lower or "insert" in lower:
        langs.append("SQL")
    if "```csharp" in text or ".net" in lower:
        langs.append("C#")
    return langs or ["Text"]


def infer_frameworks(text: str) -> list[str]:
    lower = text.lower()
    found: list[str] = []
    for hint, framework in FRAMEWORK_HINTS.items():
        if hint in lower and framework not in found:
            found.append(framework)
    return found


def infer_apis(text: str) -> list[str]:
    found: list[str] = []
    for api in API_HINTS:
        if api.lower() in text.lower() and api not in found:
            found.append(api)
    return found


def infer_vulnerabilities(text: str) -> list[str]:
    lower = text.lower()
    found: list[str] = []
    for hint, vuln in VULN_HINTS.items():
        if hint in lower and vuln not in found:
            found.append(vuln)
    return found


def infer_cwe(text: str) -> list[str]:
    return list(dict.fromkeys(CWE_PATTERN.findall(text)))


def infer_owasp(text: str) -> list[str]:
    return list(dict.fromkeys(OWASP_PATTERN.findall(text)))


def infer_keywords(text: str, title: str) -> list[str]:
    combined = f"{title} {text}".lower()
    keywords = []
    for token in re.findall(r"[a-z0-9]+", combined):
        if len(token) < 4:
            continue
        if token in {"this", "that", "with", "from", "have", "your", "into", "they", "will", "when", "using", "should", "about"}:
            continue
        keywords.append(token)
    uniq = []
    for k in keywords:
        if k not in uniq:
            uniq.append(k)
    return uniq[:30]


def infer_imports(text: str) -> list[str]:
    return [m.group(1) for m in IMPORT_PATTERN.finditer(text)]


def infer_related_classes(text: str) -> list[str]:
    classes = re.findall(r"\b([A-Z][A-Za-z0-9_]+)\b", text)
    return list(dict.fromkeys([c for c in classes if c not in {"SQL", "XSS", "CSRF", "JWT", "OAuth2", "CWE", "OWASP"}]))


def infer_related_annotations(text: str) -> list[str]:
    annotations = ANNOTATION_PATTERN.findall(text)
    return list(dict.fromkeys(annotations))


def infer_related_methods(text: str) -> list[str]:
    methods = []
    for line in text.splitlines():
        if "(" in line and ")" in line:
            token = re.search(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(", line)
            if token:
                methods.append(token.group(1))
    return list(dict.fromkeys(methods))


def split_markdown(text: str) -> list[str]:
    cleaned = normalize_text(text)
    if not cleaned:
        return []

    lines = cleaned.splitlines()
    chunks: list[str] = []
    current: list[str] = []
    current_heading: str | None = None

    def flush() -> None:
        if current:
            chunk = "\n".join(current).strip()
            if chunk:
                chunks.append(chunk)

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if current:
                current.append("")
            continue

        if re.match(r"^#{1,6}\s+", stripped):
            flush()
            current_heading = stripped.lstrip("#").strip()
            current = [stripped]
            continue

        if re.match(r"^[-*]\s+", stripped) or re.match(r"^\d+\.\s+", stripped):
            if current and len("\n".join(current)) > 2500:
                flush()
                current = [f"## {current_heading}" if current_heading else ""]
            current.append(stripped)
            continue

        if re.match(r"^```", stripped):
            if current and len("\n".join(current)) > 2500:
                flush()
                current = [f"## {current_heading}" if current_heading else ""]
            current.append(stripped)
            continue

        if current and len("\n".join(current)) > 3000:
            flush()
            current = [f"## {current_heading}" if current_heading else ""]

        current.append(stripped)

    flush()
    return chunks


def chunk_document(path: Path) -> list[dict[str, Any]]:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    cleaned = normalize_text(raw)
    title_match = re.search(r"^#\s+(.+)$", cleaned, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else path.stem.replace("_", " ")
    chunks = split_markdown(cleaned)
    result: list[dict[str, Any]] = []
    for index, chunk in enumerate(chunks):
        section = ""
        heading_lines = [ln for ln in chunk.splitlines() if re.match(r"^#{1,6}\s+", ln.strip())]
        if heading_lines:
            section = heading_lines[-1].lstrip("#").strip()
        text = re.sub(r"^#{1,6}\s+", "", chunk, flags=re.MULTILINE)
        text = normalize_text(text)
        if not text:
            continue
        record = {
            "id": str(uuid.uuid4()),
            "document": path.name,
            "title": title,
            "section": section or title,
            "chunk_index": index,
            "category": infer_category(path),
            "subcategory": infer_subcategory(path, text),
            "source": infer_source(path, text),
            "language": infer_language(text),
            "frameworks": infer_frameworks(text),
            "apis": infer_apis(text),
            "vulnerabilities": infer_vulnerabilities(text),
            "cwe": infer_cwe(text),
            "owasp": infer_owasp(text),
            "keywords": infer_keywords(text, title),
            "imports": infer_imports(text),
            "related_classes": infer_related_classes(text),
            "related_annotations": infer_related_annotations(text),
            "related_methods": infer_related_methods(text),
            "text": text,
        }
        result.append(record)
    return result


def main() -> None:
    all_records: list[dict[str, Any]] = []
    for path in sorted(SOURCE_ROOT.rglob("*.md")):
        if not path.is_file():
            continue
        all_records.extend(chunk_document(path))

    with OUTPUT_FILE.open("w", encoding="utf-8") as handle:
        for record in all_records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Wrote {len(all_records)} chunks to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
