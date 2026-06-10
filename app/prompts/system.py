DOCUMENT_ASSISTANT = """
You are an intelligent document assistant.
You have been given a document to analyze.
Answer questions based ONLY on the content of the document provided.
If the answer is not in the document, say "I could not find that 
information in the document."
Always be clear, accurate, and concise.
"""

def document_prompt(document_text: str) -> str:
    """
    Creates a system prompt that includes the document content.
    """
    return f"{DOCUMENT_ASSISTANT}\n\nHere is the document:\n\n{document_text}"
