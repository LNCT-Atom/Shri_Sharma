import hashlib
import io
import docx

def extract_docx_data(file_bytes: bytes, filename: str) -> dict:
    file_hash = hashlib.sha256(file_bytes).hexdigest()
    file_size = len(file_bytes)
    
    doc = docx.Document(io.BytesIO(file_bytes))
    full_text = []
    
    for para in doc.paragraphs:
        if para.text.strip():
            full_text.append(para.text.strip())
            
    for table in doc.tables:
        for row in table.rows:
            row_data = [cell.text.strip() for cell in row.cells if cell.text.strip()]
            if row_data:
                full_text.append(" | ".join(row_data))

    extracted_text = "\n".join(full_text)
    
    return {
        "text": extracted_text,
        "is_scanned": False,
        "file_hash": file_hash,
        "file_size": file_size,
        "file_name": filename
    }