# JavaParser - AI-Powered Java Security Analysis Tool

## 📋 Project Overview

JavaParser is a comprehensive Java Application Security Analysis platform that combines **static analysis**, **data flow visualization**, and **AI-powered vulnerability detection** to identify and explain security vulnerabilities in Java applications.

The tool leverages advanced machine learning models to analyze Java source code, detect potential security risks, and provide detailed security assessments based on industry-standard security frameworks.

## 🎯 Objectives

- **Automated Security Analysis**: Scan Java applications for security vulnerabilities using advanced AI models
- **Code Flow Visualization**: Display method dependencies and code execution paths in an interactive graph
- **Intelligent Vulnerability Detection**: Leverage Qwen 2.5 Coder LLM to identify and explain security issues
- **Security Context Integration**: Combine multiple security standards (OWASP, CWE, CERT, Spring Security) into analysis
- **Interactive Analysis**: Provide users with visual feedback and detailed security reports

## 📚 Security Documentation Standards

This project is built on industry-leading security documentation:
- OWASP Cheat Sheet Series
- CWE (Common Weakness Enumeration)
- CERT Oracle Secure Coding Standard for Java
- Spring Security Documentation
- Oracle Secure Coding Guidelines
- FindSecBugs rules
- SonarSource Java security rules

## 🚀 Getting Started

### Prerequisites

Before running the application, ensure you have:
- Java 11+ and Maven
- Node.js and npm
- Python 3.8+
- Docker or local Ollama installation

### Step 1: Install AI Models

The application uses Ollama for LLM and embedding services. Install the required models:

```bash
# Install the Qwen 2.5 Coder model (7B version)
ollama pull qwen2.5-coder:7b

# Install the Nomic Embed Text embedding model
ollama pull nomic-embed-text
```

### Step 2: Prepare Project Dependencies

Before analyzing a Java project, generate its classpath file:

```bash
# Navigate to your Java project
cd path/to/your/java/project

# Generate the classpath file
mvn dependency:build-classpath -Dmdep.outputFile=cp.txt
```

**Note**: For Spring Boot applications, this step is essential as dependencies need to be resolved. The demoApp cannot be analyzed without this setup.

### Step 3: Start ChromaDB Vector Store

Place ChromaDB in the `ai_service` directory to prevent embedding latency issues:

```bash
# This should be configured in the ai_service directory
# See ai_service/README.md for detailed setup
```

### Step 4: Start the Backend Service

Open a terminal and run:

```bash
cd backend
mvn spring-boot:run
```

The backend will start at `http://localhost:8080`

### Step 5: Start the AI Service

Open another terminal and run:

```bash
cd ai_service
uvicorn src.main:app
```

The AI service will start and connect to your Ollama models.

### Step 6: Build and Start the Frontend

Open a third terminal and run:

```bash
cd frontend
npm run build
npm run dev
```

The frontend will be available at `http://localhost:5173` or as configured by Vite.

## 📊 Using the Application

1. **Access the Web Interface**: Open your browser and navigate to `http://localhost:8080`

2. **Input Source Code Path**: Enter the root path of your Java project in the input field

3. **Visualize**: Click the "Visualize" button to generate the code dependency graph

4. **Analyze**: Scroll down to view the visualization, then click the "Analyse" button

5. **Review Results**: Wait for the AI service to complete the security analysis. The system will:
   - Parse your Java code
   - Extract method dependencies
   - Identify potential vulnerabilities
   - Generate detailed security reports with AI explanations

## 🏗️ Architecture

**JavaParser** consists of three main components:

- **Backend** (Spring Boot): REST API for code analysis and project management
- **AI Service** (Python/FastAPI): LLM-powered vulnerability analysis and embedding
- **Frontend** (React + TypeScript): Interactive visualization and user interface

## 📁 Project Structure

```
JavaParser/
├── backend/              # Spring Boot backend service
├── frontend/             # React + TypeScript frontend
├── ai_service/           # Python FastAPI AI analysis service
│   ├── knowledge/        # Security knowledge base (organized by topic)
│   │   ├── authentication/
│   │   ├── authorization/
│   │   ├── injection/
│   │   ├── cryptography/
│   │   ├── spring-security/
│   │   └── ...
│   └── src/              # AI service source code
└── README.md
```

## 🔍 Analysis Features

- **SQL Injection Detection**: Identifies SQL concatenation vulnerabilities
- **Authentication & Authorization**: Analyzes security of login and access control
- **Cryptography Analysis**: Reviews secure coding practices
- **Dependency Security**: Checks for vulnerable dependencies
- **Spring Security Configuration**: Validates Spring Security setup
- **Input Validation**: Detects unsafe input handling

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| "demoApp can't be resolved" | Run `mvn dependency:build-classpath -Dmdep.outputFile=cp.txt` in your project |
| Ollama models not found | Install models with `ollama pull qwen2.5-coder:7b` and `ollama pull nomic-embed-text` |
| Embedding latency | Ensure ChromaDB is placed in `/ai_service` directory |
| Frontend build errors | Run `npm install` in the frontend directory |

## 📝 Example Analysis Workflow

```
Input: /path/to/spring-boot-app
↓
Parser extracts methods and call chains
↓
Graph visualization displays dependencies
↓
AI analyzes security against knowledge base
↓
Output: Detailed vulnerability report with remediation
```

## 📖 Knowledge Base

The AI service includes a comprehensive security knowledge base organized by topics:
- Authentication (31 files)
- Authorization (23 files)
- Cryptography (2 files)
- Database/JDBC (2 files)
- Injection attacks (SQL, LDAP, Command) (3 files)
- Spring Security (65 files)
- Java I/O security (23 files)
- And more...

## 🤝 Contributing

Contributions are welcome! Please ensure any security knowledge updates follow OWASP and CWE standards.

## 📄 License

See LICENSE file for details.

---

**Need Help?** Check the documentation in the `ai_service/knowledge/` directory or review the security standards referenced in the project.
