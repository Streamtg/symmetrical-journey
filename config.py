import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    MONGODB_URI = os.getenv("MONGODB_URI")
    BLOGGER_API_KEY = os.getenv("BLOGGER_API_KEY")
    BLOG_ID = os.getenv("BLOG_ID")
