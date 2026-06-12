# Document Intelligence — Backend

> AI-powered document analysis API. Upload a document, ask questions, get intelligent answers using RAG.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)
![Groq](https://img.shields.io/badge/LLM-Groq-orange)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)

---

## What it does

- Upload **PDF**, **DOCX**, or **TXT** documents
- Automatically chunks and indexes documents into a vector database
- Answers questions using **RAG** (Retrieval Augmented Generation)
- Uses **query expansion** to find the most relevant content
- Maintains **conversation memory** across messages

---

## Tech Stack

| Layer | Technology |
|---|---|
| API Framework | FastAPI |
| LLM | Groq (Llama 3.3 70B) |
| Embeddings | Sentence Transformers (all-MiniLM-L6-v2) |
| Vector Database | ChromaDB |
| Document Parsing | PyMuPDF, python-docx |
| Environment | Python 3.11, uvicorn |

---

## Project Structure

```
document-intelligence/
├── app/
│   ├── core/
│   │   ├── llm.py          # LLM API calls and query expansion
│   │   ├── document.py     # PDF, DOCX, TXT reading
│   │   ├── chunker.py      # Smart semantic chunking
│   │   ├── embeddings.py   # Vector embeddings and ChromaDB
│   │   └── state.py        # Shared application state
│   ├── prompts/
│   │   └── system.py       # System prompts
│   └── routers/
│       ├── upload.py       # POST /api/upload
│       └── chat.py         # POST /api/chat
├── documents/              # Local document storage
├── api.py                  # FastAPI app entry point
├── requirements.txt
└── .env                    # API keys (never commit this)
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/eyoba45/document-intelligence.git
cd document-intelligence
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root folder:

```
GROQ_API_KEY=your-groq-api-key-here
```

Get a free Groq API key at https://console.groq.com

### 5. Run the server

```bash
uvicorn api:app --reload
```

The API will be live at `http://127.0.0.1:8000`

Visit `http://127.0.0.1:8000/docs` for interactive API documentation.

---

## API Endpoints

### `POST /api/upload`
Upload a document for analysis.

**Request:** `multipart/form-data`
- `file`: PDF, DOCX, or TXT file

**Response:**
```json
{
  "message": "Document uploaded successfully",
  "filename": "report.pdf",
  "chunks": 223
}
```

---

### `POST /api/chat`
Ask a question about the uploaded document.

**Request:**
```json
{
  "question": "Who is the project leader?"
}
```

**Response:**
```json
{
  "question": "Who is the project leader?",
  "answer": "The project leader is Eyob Mulugeta..."
}
```

---

## How RAG works in this project

```
User uploads document
        ↓
PyMuPDF / python-docx extracts text
        ↓
Smart chunker splits into semantic chunks
        ↓
Sentence Transformers converts chunks to vectors
        ↓
Vectors stored in ChromaDB
        ↓
User asks a question
        ↓
Query expansion creates 3 variations of the question
        ↓
ChromaDB finds the 8 most relevant chunks
        ↓
Groq LLM answers using only those chunks
        ↓
Answer returned to user
```

---

## Environment Variables

| Variable | Description | Required |
|---|---|---|
| `GROQ_API_KEY` | Your Groq API key | Yes |

---

## Frontend

The React frontend for this project is available at:
https://github.com/eyoba45/document-intelligence-frontend

---

## Author

**Eyob Mulugeta**
GitHub: [@eyoba45](https://github.com/eyoba45)