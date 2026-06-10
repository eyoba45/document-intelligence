import re

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list:
    """
    Split text into chunks. Tries to split by sections first,
    falls back to character splitting for large sections.
    """
    # First try to split by sections
    sections = split_by_sections(text)

    chunks = []
    for section in sections:
        # If section is small enough, keep it as one chunk
        if len(section) <= chunk_size:
            if section.strip():
                chunks.append(section.strip())
        else:
            # If section is too large, split it by characters
            sub_chunks = split_by_characters(section, chunk_size, overlap)
            chunks.extend(sub_chunks)

    return chunks


def split_by_sections(text: str) -> list:
    """
    Split text by headings and section markers.
    """
    # Split on patterns like "Chapter", "1.", "2.", empty lines before caps
    pattern = r'\n(?=Chapter|\d+\.\d*\s+[A-Z]|[A-Z][A-Z\s]{3,})'
    sections = re.split(pattern, text)
    return [s.strip() for s in sections if s.strip()]


def split_by_characters(text: str, chunk_size: int, overlap: int) -> list:
    """
    Simple character-based splitting with overlap.
    """
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        if chunk.strip():
            chunks.append(chunk.strip())
        start += chunk_size - overlap

    return chunks