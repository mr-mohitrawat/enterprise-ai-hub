# src/app/services/chat.py

from app.agents.runner import chat as run_agent_chat
from app.schemas.chat import ChatRequest, ChatResponse


async def create_chat_response(request: ChatRequest) -> ChatResponse:
    session_id, reply = await run_agent_chat(
        user_id=request.user_id,
        message=request.message,
        session_id=request.session_id,
    )

    return ChatResponse(session_id=session_id, reply=reply)