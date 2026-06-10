from groq import Groq
from dotenv import load_dotenv
from app.prompts.system import DOCUMENT_ASSISTANT
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask(user_message: str) -> str:
    """
    Send a message to the AI and get a response back.
    
    Args:
        user_message: The message to send to the AI
        
    Returns:
        The AI's response as a string
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": DOCUMENT_ASSISTANT},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content