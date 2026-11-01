import hashlib
import io
import pdfplumber

def extract_pdf_data(file_bytes: bytes, filename: str) -> dict:
    file_hash = hashlib.sha256(file_bytes).hexdigest()
    file_size = len(file_bytes)
    
    extracted_text = ""
    # Wrap bytes in BytesIO so pdfplumber can seek/read it as a stream
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"

    is_scanned = len(extracted_text.strip()) < 50
    return {
        "text": extracted_text,
        "is_scanned": is_scanned,
        "file_hash": file_hash,
        "file_size": file_size,
        "file_name": filename
    }