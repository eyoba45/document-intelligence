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
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000" ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(upload.router, prefix="/api", tags=["Upload"])
app.include_router(chat.router, prefix="/api", tags=["Chat"])

@app.get("/")
if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("api:app", host="0.0.0.0", port=port)
