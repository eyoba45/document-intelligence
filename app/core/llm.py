from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation_history = []

def expand_query(question: str) -> list:
    """
    Ask the AI to rephrase the question in 3 different ways
    to improve search results.
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """Generate 3 different ways to search for the 
                answer to this question. Return only the 3 search queries,
                one per line, nothing else."""
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )
    
    queries = response.choices[0].message.content.strip().split("\n")
    queries.append(question)  # always include original
    return queries


def ask(user_message: str, system_prompt: str) -> str:
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt}
        ] + conversation_history
    )

    ai_reply = response.choices[0].message.content

    conversation_history.append({
        "role": "assistant",
        "content": ai_reply
    })

    return ai_reply