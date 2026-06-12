from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import upload, chat

app = FastAPI(
    title="Document Intelligence API",
    description="Upload a document and ask questions about it",
    version="1.0.0"
)

# Allow React frontend to talk to the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000" , "https://document-intelligence-frontend-snowy.vercel.app"],
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
