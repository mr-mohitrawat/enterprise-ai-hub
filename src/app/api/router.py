from fastapi import APIRouter
from app.api.routes.v1.chat import router as chat_router

router = APIRouter()

router.include_router(chat_router, prefix="/v1", tags = ["chat"])