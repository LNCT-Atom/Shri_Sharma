# 📄 Smart AI Resume Parser

An end-to-end resume parsing system that ingests unstructured PDF and DOCX files, segments career information, and outputs a strictly validated JSON structure matching your schema. Built using Python, Streamlit, Google GenAI (`gemini-3.8-flash`), and Pydantic v2, packaged for standalone Windows executable distribution.

---

## 🚀 Key Features

- **Document Extraction**: Seamless text and table extraction for `.pdf` and `.docx` using `pdfplumber` and `python-docx`.
- **Strict Skill Isolation**: Technologies in `technical_skills.technologies` originate strictly from dedicated skills sections and are not mixed with project or work experience tools.
- **Strict JSON Schema**: Guaranteed schema conformity using Pydantic models with field typing, timestamps, SHA-256 hash generation, and file size metadata.
- **Interactive Desktop UI**: Streamlit dashboard supporting drag-and-drop file upload, structured visual inspection, and JSON export.
- **Desktop Executable Ready**: Bundled with PyInstaller to run without requiring a pre-installed Python runtime on the client machine.

---

## 📂 Project Hierarchy

```text
og-resume-parser/
│
├── .env                          # API key configuration
├── requirements.txt              # Project dependencies
├── run_app.py                    # Entry point launcher for Streamlit & PyInstaller
├── test_backend.py               # Direct CLI test script for pipeline evaluation
│
├── src/
│   ├── __init__.py
│   ├── schemas.py                # Pydantic v2 resume schema definition
│   ├── orchestrator.py           # Pipeline controller (routing, hashing, parsing)
│   │
│   ├── extractors/
│   │   ├── __init__.py
│   │   ├── pdf_extractor.py      # Stream-based PDF text and metadata extraction
│   │   └── docx_extractor.py     # DOCX paragraph and table extraction
│   │
│   └── parsers/
│       ├── __init__.py
│       ├── section_mapper.py     # Header normalization dictionary
│       ├── heuristic_parser.py   # Deterministic regex for contact data
│       └── llm_parser.py         # Google GenAI structured JSON parser
│
└── ui/
    ├── __init__.py
    └── streamlit_app.py          # Streamlit UI implementation
```

---

## 📋 JSON Output Structure

The output strictly follows this structure:

```json
{
  "profile": {
    "full_name": "Vivek Awasthi",
    "email": "vivekawasthi2007@gmail.com",
    "phone": "+91 8516803872",
    "location": "Chhatarpur, Madhya Pradesh",
    "linkedin_url": "https://linkedin.com/in/vivek-awasthi-33656a329",
    "github_url": "https://github.com/vivekawasthi2007",
    "portfolio_url": null,
    "summary": null
  },
  "education": [],
  "technical_skills": {
    "technologies": ["Python", "Django", "JavaScript", "SQLite"]
  },
  "projects": [
    {
      "title": "Airlines Management System",
      "role": null,
      "description": "Salesforce-based system managing flight bookings, passenger records, and airline operations.",
      "technologies": ["Salesforce", "Apex", "Python", "Django", "Tailwind CSS"]
    }
  ],
  "experience": [
    {
      "company": "LNCT Group of Colleges",
      "role": "Volunteer - Training & Placement (T&P) Department",
      "experience_type": "volunteer",
      "start_date": null,
      "end_date": null,
      "description": "Assisted with placement drives and coordinated with recruiters.",
      "technologies": []
    }
  ],
  "certifications": [],
  "achievements": [],
  "metadata": {
    "parser_version": "1.0",
    "status": "completed",
    "created_at": "2026-11-01T10:00:00.000000+00:00",
    "parsed_at": "2026-11-01T10:00:00.000000+00:00",
    "file_name": "resume.pdf",
    "file_hash": "182301160d61f331e1abbe80bde16b6a874a77de917c7e9f2f31272c5d36697a",
    "file_size_bytes": 135772,
    "ai_called_for_projects_or_experience": true,
    "is_scanned_pdf": false
  }
}
```

---

## ⚙️ Installation & Setup

### 1. Virtual Environment Setup

```powershell
# Clone or navigate to the directory
cd D:\og-resume-parser

# Create virtual environment
python -m venv venv

# Activate virtual environment (PowerShell)
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
pip install pydantic pdfplumber python-docx python-dotenv google-genai streamlit pyinstaller
```

### 3. Setup Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

---

## 💻 Running the Application

### Option 1: Run the Desktop GUI
```powershell
python run_app.py
```
This launches the Streamlit interface locally at `http://localhost:8501`.

### Option 2: Run CLI Backend Verification
```powershell
python test_backend.py "path\to\resume.pdf"
```
Directly outputs the parsed JSON to the console and saves `parsed_result.json` in the root folder.

---

## 📦 Packaging to Windows Executable (.exe)

Compile into a standalone executable directory:

```powershell
python -m PyInstaller --noconfirm --onedir --windowed --copy-metadata streamlit --collect-all streamlit --add-data "ui;ui" --add-data "src;src" --add-data ".env;." run_app.py
```

- **Output Location**: `dist\run_app\run_app.exe`
- When distributing the folder, make sure the `.env` file exists alongside `run_app.exe` inside `dist\run_app\`.