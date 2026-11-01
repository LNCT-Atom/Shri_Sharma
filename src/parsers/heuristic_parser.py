import re
from typing import Dict, Optional

EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
PHONE_REGEX = r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{3,5}\)?[-.\s]?\d{3,5}[-.\s]?\d{3,5}'
LINKEDIN_REGEX = r'https?://(?:www\.)?linkedin\.com/in/[a-zA-Z0-9_-]+/?'
GITHUB_REGEX = r'https?://(?:www\.)?github\.com/[a-zA-Z0-9_-]+/?'

def extract_basic_profile(text: str) -> Dict[str, Optional[str]]:
    email = re.search(EMAIL_REGEX, text)
    phone = re.search(PHONE_REGEX, text)
    linkedin = re.search(LINKEDIN_REGEX, text)
    github = re.search(GITHUB_REGEX, text)
    
    return {
        "email": email.group(0) if email else None,
        "phone": phone.group(0).strip() if phone else None,
        "linkedin_url": linkedin.group(0) if linkedin else None,
        "github_url": github.group(0) if github else None
    }