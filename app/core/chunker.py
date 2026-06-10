def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list:
    """
    Split a large text into smaller overlapping chunks.
    
    Args:
        text: The full document text
        chunk_size: How many characters per chunk
        overlap: How many characters to repeat between chunks
                 so we don't lose context at the edges
    
    Returns:
        A list of text chunks
    """
    chunks = []
    start = 0

    while start < len(text):
        # Take a chunk of text
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        # Move forward but overlap a little
        start += chunk_size - overlap

    return chunks