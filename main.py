from app.core.llm import ask
from app.core.document import read_document
from app.prompts.system import document_prompt

# Read the document
document = read_document("documents/sample.txt")

# Create a system prompt that includes the document
system = document_prompt(document)

# Ask questions about the document
print(ask("When was ASTU established?", system))
print("---")
print(ask("How many students are enrolled?", system))
print("---")
print(ask("What is the size of the main campus?", system))
print("---")
print(ask("Who is the president of the United States?", system))