import chromadb
from sentence_transformers import SentenceTransformer

# Load the embedding model
# This runs locally on your computer - no API needed
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create a ChromaDB client - this is your vector database
client = chromadb.Client()

def create_collection(chunks: list, collection_name: str = "document"):
    """
    Take a list of text chunks, convert them to embeddings,
    and store them in ChromaDB.
    """
    # Delete old collection if it exists
    try:
        client.delete_collection(collection_name)
    except Exception:
        pass

    # Create a fresh collection
    collection = client.create_collection(collection_name)

    # Add all chunks to the collection
    collection.add(
        documents=chunks,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )

    print(f"Stored {len(chunks)} chunks in vector database")
    return collection


def find_relevant_chunks_expanded(
    questions: list, 
    collection, 
    n_results: int = 3
) -> list:
    """
    Search using multiple query variations and combine results.
    """
    all_chunks = []
    seen = set()

    for question in questions:
        results = collection.query(
            query_texts=[question],
            n_results=n_results
        )
        for chunk in results["documents"][0]:
            # Avoid duplicates
            if chunk not in seen:
                seen.add(chunk)
                all_chunks.append(chunk)

    return all_chunks