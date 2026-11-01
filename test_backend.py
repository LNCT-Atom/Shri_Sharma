import json
import sys

from src.orchestrator import ResumeParserOrchestrator


def test_resume_file(file_path: str):
    orchestrator = ResumeParserOrchestrator()
    
    with open(file_path, "rb") as f:
        file_bytes = f.read()

    print(f"Parsing: {file_path} ...")
    result = orchestrator.process_file(file_bytes, file_path)
    
    # Pretty print the final JSON
    output_json = result.model_dump_json(indent=2)
    print("\n--- Extracted JSON Output ---\n")
    print(output_json)

    # Save to disk as an artifact
    output_filename = "parsed_result.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(output_json)
    print(f"\nSaved output to {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_backend.py <path_to_resume.pdf_or_docx>")
    else:
        test_resume_file(sys.argv[1])