from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URL"))

try:
    client.admin.command("ping")
    print("MongoDB Atlas connected")
except Exception as e:
    print("MongoDB connection failed")
    print(e)

db = client["readerai"]

documents = db["documents"]
users = db["users"]
chats = db["chats"]