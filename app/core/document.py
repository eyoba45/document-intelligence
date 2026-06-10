def read_document(file_path: str) -> str:
    """
    Read a text document and return its content.
    
    Args:
        file_path: Path to the document
        
    Returns:
        The document content as a string
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content