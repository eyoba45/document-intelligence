from groq import Groq
from dotenv import load_dotenv
from app.prompts.system import DOCUMENT_ASSISTANT
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# This list stores the conversation history
conversation_history = []

def ask(user_message: str) -> str:
    # Add the user's message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    # Send the full history to the AI every time
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": DOCUMENT_ASSISTANT}
        ] + conversation_history
    )

    # Get the AI reply
    ai_reply = response.choices[0].message.content

    # Add the AI reply to history too
    conversation_history.append({
        "role": "assistant",
        "content": ai_reply
    })

    return ai_reply