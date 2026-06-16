from fastapi import APIRouter
from pydantic import BaseModel

from app.services.embedder import create_embeddings
from app.store.vector_store import search_vectors
from app.services.llm import generate_answer
from app.database.database import chats


router = APIRouter()


class Question(BaseModel):
    question: str


@router.post("/ask")
def ask_question(data: Question):

    question_vector = create_embeddings(
        [data.question]
    )[0]


    context = search_vectors(
        question_vector
    )


    answer = generate_answer(
        data.question,
        context
    )


    result = chats.insert_one(
        {
            "question":data.question,
            "answer":answer
        }
    )


    return {
        "chat_id":str(result.inserted_id),
        "question":data.question,
        "answer":answer
    }