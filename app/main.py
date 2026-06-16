from fastapi import FastAPI
from app.store.vector_store import load_vectors
from app.routes import upload, ask, history, auth
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
load_vectors()
app.include_router(upload.router)
app.include_router(ask.router)
app.include_router(history.router)
app.include_router(auth.router)
app.add_middleware(SessionMiddleware, secret_key="readerai_session_secret")
@app.get("/")
def home():
    return {"message":"AskQuestion backend running"}