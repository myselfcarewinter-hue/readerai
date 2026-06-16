from fastapi import APIRouter, Request
from starlette.config import Config
from authlib.integrations.starlette_client import OAuth

from app.database.database import users
from app.services.token import create_access_token


router = APIRouter()


config = Config(".env")


oauth = OAuth(config)


oauth.register(
    name="google",
    client_id=config("GOOGLE_CLIENT_ID"),
    client_secret=config("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope":"openid email profile"
    }
)


@router.get("/auth/google")
async def login(request: Request):

    redirect_uri = (
        "http://localhost:8000/auth/google/callback"
    )

    return await oauth.google.authorize_redirect(
        request,
        redirect_uri
    )


@router.get("/auth/google/callback")
async def callback(request: Request):

    token = await oauth.google.authorize_access_token(
        request
    )

    user = token["userinfo"]


    users.update_one(
        {
            "email":user["email"]
        },
        {
            "$set":{
                "name":user["name"],
                "email":user["email"],
                "picture":user["picture"]
            }
        },
        upsert=True
    )


    access_token = create_access_token(
        {
            "email":user["email"]
        }
    )


    return {
        "access_token":access_token,
        "user":user
    }