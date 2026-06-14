import chromadb
from chromadb.utils import embedding_functions

ef = embedding_functions.DefaultEmbeddingFunction()
client = chromadb.Client()

def create_collection(chunks: list, collection_name: str = "document"):
    # Clean chunks
    clean_chunks = [c.strip() for c in chunks if c and len(c.strip()) > 10]
    
    # Last resort fallback
    if not clean_chunks:
        clean_chunks = ["Document content could not be extracted properly."]
    
    try:
        client.delete_collection(collection_name)
    except:
        pass

    collection = client.create_collection(
        name=collection_name,
        embedding_function=ef
    )

    # Add in batches of 100 to avoid memory issues
    batch_size = 100
    for i in range(0, len(clean_chunks), batch_size):
        batch = clean_chunks[i:i + batch_size]
        batch_ids = [f"chunk_{i + j}" for j in range(len(batch))]
        collection.add(
            documents=batch,
            ids=batch_ids
        )

    print(f"Stored {len(clean_chunks)} chunks in vector database")
    return collection


def find_relevant_chunks(question: str, collection, n_results: int = 3) -> list:
    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )
    return results["documents"][0]


def find_relevant_chunks_expanded(
    questions: list,
    collection,
    n_results: int = 3
) -> list:
    all_chunks = []
    seen = set()

    for question in questions:
        try:
            results = collection.query(
                query_texts=[question],
                n_results=n_results
            )
            for chunk in results["documents"][0]:
                if chunk not in seen:
                    seen.add(chunk)
                    all_chunks.append(chunk)
        except:
            pass

    return all_chunks
