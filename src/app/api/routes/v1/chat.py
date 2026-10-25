from fastapi import APIRouter
from pydantic import BaseModel
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat import create_chat_response, get_chat_history, all_sessions
from app.core.config import settings
from app.schemas.chat import ChatHistoryRequest, ChatHistoryResponse, ChatSessionsRequest, ChatSessionsResponse
router = APIRouter(
    prefix="/chat"
)

@router.post("/run", response_model = ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    return await create_chat_response(user_id = request.user_id, session_id = request.session_id, message = request.message)

@router.get("/sessions", response_model=ChatSessionsResponse)
async def get_all_sessions(request: ChatSessionsRequest):
    return await all_sessions(request.user_id)

@router.get("/messages", response_model=ChatHistoryResponse)
async def chat_history(request: ChatHistoryRequest) -> ChatHistoryResponse:
    return await get_chat_history(user_id = request.user_id, session_id = request.session_id)
