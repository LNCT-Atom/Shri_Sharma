from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, HttpUrl


class Profile(BaseModel):
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    portfolio_url: Optional[str] = None
    summary: Optional[str] = None

class EducationItem(BaseModel):
    institution: Optional[str] = None
    degree: Optional[str] = None
    field_of_study: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    grade_or_gpa: Optional[str] = None

class TechnicalSkills(BaseModel):
    technologies: List[str] = Field(default_factory=list)

class Project(BaseModel):
    title: str
    role: Optional[str] = None
    description: Optional[str] = None
    technologies: List[str] = Field(default_factory=list)

class Experience(BaseModel):
    company: str
    role: Optional[str] = None
    experience_type: Optional[str] = "full_time"  # internship, volunteer, other, etc.
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: Optional[str] = None
    technologies: List[str] = Field(default_factory=list)

class Metadata(BaseModel):
    parser_version: str = "1.0"
    status: str = "completed"
    created_at: str
    parsed_at: str
    file_name: str
    file_hash: str
    file_size_bytes: int
    ai_called_for_projects_or_experience: bool = True
    is_scanned_pdf: bool = False

class ResumeOutput(BaseModel):
    profile: Profile
    education: List[EducationItem] = Field(default_factory=list)
    technical_skills: TechnicalSkills
    projects: List[Project] = Field(default_factory=list)
    experience: List[Experience] = Field(default_factory=list)
    certifications: List[str] = Field(default_factory=list)
    achievements: List[str] = Field(default_factory=list)
    metadata: Metadata