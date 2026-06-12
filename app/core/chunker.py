import re

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> list:
    """
    Smart chunking that respects sentence and paragraph boundaries.
    """
    # Step 1: Clean the text
    text = clean_text(text)
    
    # Step 2: Split into paragraphs first
    paragraphs = split_into_paragraphs(text)
    
    # Step 3: Group paragraphs into chunks
    chunks = group_into_chunks(paragraphs, chunk_size, overlap)
    
    # Step 4: Final filter
    chunks = [c for c in chunks if c and len(c.strip()) > 20]
    
    return chunks


def clean_text(text: str) -> str:
    """
    Remove noise from extracted text.
    """
    # Remove excessive whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' {2,}', ' ', text)
    # Remove page numbers like "Page 1 of 10"
    text = re.sub(r'Page \d+ of \d+', '', text)
    # Remove standalone numbers (page numbers)
    text = re.sub(r'\n\d+\n', '\n', text)
    return text.strip()


def split_into_paragraphs(text: str) -> list:
    """
    Split text into paragraphs using blank lines as boundaries.
    """
    paragraphs = text.split('\n\n')
    result = []
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        # If paragraph is very long, split by sentences
        if len(para) > 500:
            sentences = split_into_sentences(para)
            result.extend(sentences)
        else:
            result.append(para)
    
    return result


def split_into_sentences(text: str) -> list:
    """
    Split text into individual sentences.
    """
    # Split on period, question mark, exclamation followed by space
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip()]


def group_into_chunks(paragraphs: list, chunk_size: int, overlap: int) -> list:
    """
    Group paragraphs into chunks of roughly chunk_size characters.
    Use overlap to avoid losing context at boundaries.
    """
    chunks = []
    current_chunk = ""
    overlap_buffer = ""

    for paragraph in paragraphs:
        # If adding this paragraph exceeds chunk size
        if len(current_chunk) + len(paragraph) > chunk_size:
            if current_chunk:
                # Save current chunk
                chunks.append(current_chunk.strip())
                
                # Keep last part as overlap for next chunk
                words = current_chunk.split()
                overlap_words = words[-overlap//5:] if len(words) > overlap//5 else words
                overlap_buffer = " ".join(overlap_words)
                
                # Start new chunk with overlap
                current_chunk = overlap_buffer + "\n\n" + paragraph
            else:
                # Single paragraph too long — add it anyway
                current_chunk = paragraph
        else:
            # Add paragraph to current chunk
            if current_chunk:
                current_chunk += "\n\n" + paragraph
            else:
                current_chunk = paragraph

    # Don't forget the last chunk
    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks