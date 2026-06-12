from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import upload, chat
import os

app = FastAPI(
    title="Document Intelligence API",
    description="Upload a document and ask questions about it",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/api", tags=["Upload"])
app.include_router(chat.router, prefix="/api", tags=["Chat"])

@app.get("/")
def home():
    return {
        "message": "Document Intelligence API is running",
        "docs": "Visit /docs to see all endpoints"
    }
