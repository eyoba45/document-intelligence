import chromadb
from chromadb.utils import embedding_functions

# Use a much lighter embedding function
# This uses chromadb's built-in default which is tiny
ef = embedding_functions.DefaultEmbeddingFunction()

client = chromadb.Client()

def create_collection(chunks: list, collection_name: str = "document"):
    try:
        client.delete_collection(collection_name)
    except:
        pass

    collection = client.create_collection(
        name=collection_name,
        embedding_function=ef
    )

    collection.add(
        documents=chunks,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )

    print(f"Stored {len(chunks)} chunks in vector database")
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
        results = collection.query(
            query_texts=[question],
            n_results=n_results
        )
        for chunk in results["documents"][0]:
            if chunk not in seen:
                seen.add(chunk)
                all_chunks.append(chunk)

    return all_chunks
