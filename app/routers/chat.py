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

    # Expand query into multiple variations
    queries = expand_query(request.question)

    # Get more chunks — 8 instead of 3
    relevant_chunks = find_relevant_chunks_expanded(
        queries, app_state.current_collection, n_results=8
    )

    # Build context
    context = "\n\n---\n\n".join(relevant_chunks)

    # Build prompt
    system = document_prompt(context)

    # Get answer
    response = ask(request.question, system)

    return {
        "question": request.question,
        "answer": response
    }