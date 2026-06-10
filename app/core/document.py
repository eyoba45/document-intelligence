import fitz  # this is PyMuPDF
import os

def read_document(file_path: str) -> str:
    """
    Read a document and return its text content.
    Supports PDF and TXT files.
    """
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return read_pdf(file_path)
    elif extension == ".txt":
        return read_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {extension}")


def read_pdf(file_path: str) -> str:
    """
    Extract all text from a PDF file.
    """
    text = ""
    doc = fitz.open(file_path)

    for page in doc:
        text += page.get_text()

    doc.close()
    return text


def read_txt(file_path: str) -> str:
    """
    Read a plain text file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()