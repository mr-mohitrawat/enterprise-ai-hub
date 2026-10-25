# src/app/services/chat.py

from app.agents.runner import chat as run_agent_chat
from app.schemas.chat import ChatRequest, ChatResponse, ChatHistoryResponse
from fastapi import HTTPException

from app.agents.runner import session_service
from app.core.config import settings
from app.schemas.chat import ChatSessionsResponse


async def create_chat_response(*, user_id: str, session_id: str, message: str) -> ChatResponse:
    session_id, reply = await run_agent_chat(
        user_id=user_id,
        message=message,
        session_id=session_id,
    )

    return ChatResponse(session_id=session_id, reply=reply)


async def get_chat_history(*, user_id: str, session_id: str) -> ChatHistoryResponse:
    session = await session_service.get_session(
        app_name=settings.app_name,
        user_id=user_id,
        session_id=session_id,
    )

    if session is None:
        raise HTTPException(status_code=404, detail="Chat session not found")

    messages = []

    for event in session.events:
        if not event.content or not event.content.parts:
            continue

        text = "".join(
            part.text
            for part in event.content.parts
            if part.text
        )

        if text:
            messages.append({
                "role": event.author,
                "content": text,
            })

    return ChatHistoryResponse(
                session_id = session.id,
                messages = messages,
            )

async def all_sessions(user_id: str):
    result = await session_service.list_sessions(
        app_name=settings.app_name,
        user_id=user_id,
    )
    return ChatSessionsResponse(user_id = user_id, sessions = [{"id": session.id} for session in result.sessions])