from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.llm import ask, expand_query
from app.core.embeddings import find_relevant_chunks_expanded
from app.prompts.system import document_prompt
from app.core.state import app_state

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

@router.post("/chat")
async def chat(request: QuestionRequest):
    if not app_state.document_loaded or app_state.current_collection is None:
        raise HTTPException(
            status_code=400,
            detail="Please upload a document first"
        )

    queries = expand_query(request.question)
    relevant_chunks = find_relevant_chunks_expanded(
        queries, app_state.current_collection, n_results=3
    )

    context = "\n\n".join(relevant_chunks)
    system = document_prompt(context)
    response = ask(request.question, system)

    return {
        "question": request.question,
        "answer": response
    }