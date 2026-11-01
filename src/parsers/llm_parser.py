import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
from src.schemas import ResumeOutput

load_dotenv(override=True)

class ResumeLLMParser:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY or GOOGLE_API_KEY is not defined in your .env file.")
        
        self.client = genai.Client(api_key=api_key)
        self.model_name = "gemini-3.8-flash"

    def parse_resume(self, resume_text: str, metadata_defaults: dict) -> ResumeOutput:
        prompt = f"""
        You are an expert resume parsing engine.
        Analyze the raw resume text below and extract all entities strictly into the specified JSON format.

        JSON Schema requirements:
        - profile: {{ full_name, email, phone, location, linkedin_url, github_url, portfolio_url, summary }}
        - education: list of {{ institution, degree, field_of_study, start_date, end_date, grade_or_gpa }}
        - CRITICAL EXTRACTION RULES:
        1. 'technical_skills':
           - STRICT ISOLATION RULE: Populate 'technical_skills.technologies' ONLY with skills, tools, languages, and frameworks explicitly written under the candidate's designated 'Skills' / 'Technical Skills' / 'Core Competencies' section.
           - DO NOT infer, aggregate, or pull any technologies from 'Projects' or 'Experience' / 'Work History' sections into 'technical_skills'. If a tool is only mentioned in a project or work experience, DO NOT add it to 'technical_skills.technologies'.
        - projects: list of {{ title, role, description, technologies: [] }}
        - experience: list of {{ company, role, experience_type, start_date, end_date, description, technologies: [] }}
        - certifications: []
        - achievements: []
        - metadata:
            parser_version: "1.0"
            status: "completed"
            created_at: "{metadata_defaults.get('timestamp')}"
            parsed_at: "{metadata_defaults.get('timestamp')}"
            file_name: "{metadata_defaults.get('file_name')}"
            file_hash: "{metadata_defaults.get('file_hash')}"
            file_size_bytes: {metadata_defaults.get('file_size_bytes')}
            ai_called_for_projects_or_experience: true
            is_scanned_pdf: {str(metadata_defaults.get('is_scanned', False)).lower()}

        Resume Raw Text:
        \"\"\"{resume_text}\"\"\"
        """

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ResumeOutput,
                temperature=0.1
            ),
        )

        return ResumeOutput.model_validate_json(response.text)