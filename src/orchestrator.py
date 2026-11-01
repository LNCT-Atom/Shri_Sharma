import os
from datetime import datetime, timezone
from src.extractors.pdf_extractor import extract_pdf_data
from src.extractors.docx_extractor import extract_docx_data
from src.parsers.llm_parser import ResumeLLMParser
from src.schemas import ResumeOutput

class ResumeParserOrchestrator:
    def __init__(self):
        self.parser = ResumeLLMParser()

    def process_file(self, file_bytes: bytes, filename: str) -> ResumeOutput:
        ext = os.path.splitext(filename)[1].lower()
        
        if ext == ".pdf":
            extracted = extract_pdf_data(file_bytes, filename)
        elif ext in [".docx", ".doc"]:
            extracted = extract_docx_data(file_bytes, filename)
        else:
            raise ValueError(f"Unsupported file format: {ext}. Only .pdf and .docx are supported.")

        if not extracted["text"].strip():
            raise ValueError("The uploaded document contains no readable text. It may be an image-only scan.")

        metadata_defaults = {
            "file_name": extracted["file_name"],
            "file_hash": extracted["file_hash"],
            "file_size_bytes": extracted["file_size"],
            "is_scanned": extracted["is_scanned"],
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        # Run extraction through the schema-guided LLM
        parsed_result = self.parser.parse_resume(
            resume_text=extracted["text"],
            metadata_defaults=metadata_defaults
        )

        return parsed_result