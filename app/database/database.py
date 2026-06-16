from pymongo import MongoClient
import os


MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb://readerai_db:27017"
)

client = MongoClient(MONGO_URL)


db = client["readerai"]


documents = db["documents"]

users = db["users"]

chats = db["chats"]