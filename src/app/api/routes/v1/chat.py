from fastapi import APIRouter
from pydantic import BaseModel
from app.schemas.chat import ChatRequest, ChatResponse
router = APIRouter(
    prefix="/chat"
)

@router.post("/", response_model = ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    return ChatResponse(reply=f"You said: {request.message}")