from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from routers import endpoints

load_dotenv()

app = FastAPI()

# MongoDB 연결 설정
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_DB = os.getenv("MONGO_DB", "emotion_db")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "emotion_logs")

mongo_client = AsyncIOMotorClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}")
db = mongo_client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# 라우터 등록
app.include_router(endpoints.router)
