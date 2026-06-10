from app.core.document import read_document
from app.core.chunker import chunk_text
from app.core.embeddings import create_collection, find_relevant_chunks_expanded
from app.core.llm import ask, expand_query
from app.prompts.system import document_prompt

# Step 1: Read and chunk the document
document = read_document("documents/test.pdf")
chunks = chunk_text(document)
print(f"✅ Document loaded: {len(chunks)} chunks")

# Step 2: Store chunks in vector database
collection = create_collection(chunks)
print("✅ Vector database ready")

print("\n💬 Ask anything about your document. Type 'exit' to quit.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Step 3: Expand the query into multiple variations
    queries = expand_query(question)

    # Step 4: Search with all variations
    relevant_chunks = find_relevant_chunks_expanded(
        queries, collection, n_results=3
    )

    # Step 5: Build context and ask
    context = "\n\n".join(relevant_chunks)
    system = document_prompt(context)
    response = ask(question, system)
    print(f"\nAI: {response}\n")