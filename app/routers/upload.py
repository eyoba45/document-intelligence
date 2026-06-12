from fastapi import APIRouter, UploadFile, File, HTTPException
from app.core.document import read_document
from app.core.chunker import chunk_text
from app.core.embeddings import create_collection
from app.core.state import app_state
import shutil
import os

router = APIRouter()

@router.post("/api/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".txt")):
        raise HTTPException(
            status_code=400,
            detail="Only PDF and TXT files are supported"
        )

    temp_path = f"documents/temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = read_document(temp_path)
    chunks = chunk_text(text, chunk_size=1000, overlap=100)

    app_state.current_collection = create_collection(chunks)
    app_state.document_loaded = True

    os.remove(temp_path)

    return {
        "message": "Document uploaded successfully",
        "filename": file.filename,
        "chunks": len(chunks)
    }
