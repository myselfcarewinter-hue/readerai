from fastapi import APIRouter, UploadFile, File
from app.services.extractor import extract_text
from app.services.chunker import create_chunks
from app.services.embedder import create_embeddings
from app.store.vector_store import save_vectors
from app.database.database import documents

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    path = "uploaded.pdf"

    with open(path,"wb") as f:
        f.write(await file.read())

    text = extract_text(path)
    chunks = create_chunks(text)
    vectors = create_embeddings(chunks)

    save_vectors(vectors, chunks)
    result = documents.insert_one(
    {
        "filename":file.filename,
        "chunks":len(chunks)
    }
    )
    return {
    "document_id":str(result.inserted_id),
    "filename":file.filename,
    "characters":len(text),
    "chunks":len(chunks),
    "vectors":len(vectors)
}