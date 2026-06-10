from fastapi import FastAPI
from app.routers import upload, chat

app = FastAPI(
    title="Document Intelligence API",
    description="Upload a document and ask questions about it",
    version="1.0.0"
)

# Register the routers
app.include_router(upload.router, prefix="/api", tags=["Upload"])
app.include_router(chat.router, prefix="/api", tags=["Chat"])

@app.get("/")
def home():
    return {
        "message": "Document Intelligence API is running",
        "docs": "Visit /docs to see all endpoints"
    }