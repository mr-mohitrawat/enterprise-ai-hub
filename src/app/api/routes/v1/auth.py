from fastapi import APIRouter
from pydantic import BaseModel
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat import create_chat_response, get_chat_history, all_sessions
from app.core.config import settings
from app.schemas.chat import ChatHistoryRequest, ChatHistoryResponse, ChatSessionsRequest, ChatSessionsResponse
router = APIRouter(
    prefix="/auth"
)


@router.post("/sighup")
def signup():
    pass

@router.post("/login")
def login():
    pass