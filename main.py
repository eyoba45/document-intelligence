from app.core.document import read_document
from app.core.chunker import chunk_text

# Read the document
document = read_document("documents/test.pdf")
print(f"Document loaded: {len(document)} characters")

# Chunk it
chunks = chunk_text(document)
print(f"Split into: {len(chunks)} chunks")
print("---")

# Show the first 3 chunks
for i, chunk in enumerate(chunks[:3]):
    print(f"Chunk {i+1}:")
    print(chunk)
    print("---")