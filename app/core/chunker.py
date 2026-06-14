import re

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> list:
    # Step 1: Aggressively clean the text
    text = clean_text(text)
    
    if not text.strip():
        return ["No readable content found in document."]
    
    # Step 2: Simple character chunking — most reliable across platforms
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()
        if chunk and len(chunk) > 30:
            chunks.append(chunk)
        start += chunk_size - overlap
    
    # Step 3: If still empty return the whole text as one chunk
    if not chunks:
        chunks = [text[:4000]]
    
    return chunks


def clean_text(text: str) -> str:
    # Remove null bytes
    text = text.replace('\x00', '')
    # Remove excessive whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' {2,}', ' ', text)
    # Remove non-printable characters
    text = re.sub(r'[^\x20-\x7E\n\t\u1200-\u137F]', ' ', text)
    return text.strip()
