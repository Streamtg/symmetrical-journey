from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGODB_URI)
db = client["telegram_files"]
collection = db["archivos"]

async def save_to_db(hash_code: str, file_id: str):
    collection.insert_one({
        "hash": hash_code,
        "file_id": file_id,
        "timestamp": datetime.now()
    })

async def get_file_id(hash_code: str) -> str:
    doc = collection.find_one({"hash": hash_code})
    return doc["file_id"] if doc else None
