from fastapi import APIRouter
from pydantic import BaseModel
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat import create_chat_response
from app.core.config import settings
router = APIRouter(
    prefix="/chat"
)

@router.post("/", response_model = ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    return await create_chat_response(request)