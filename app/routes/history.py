from fastapi import APIRouter
from app.database.database import chats


router = APIRouter()


@router.get("/history")
def get_history():

    data = []

    for chat in chats.find():

        data.append(
            {
                "id": str(chat["_id"]),
                "question": chat["question"],
                "answer": chat["answer"]
            }
        )

    return data