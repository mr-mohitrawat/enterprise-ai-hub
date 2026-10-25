# src/app/agents/runner.py
import os
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from google.genai import types

from app.agents.chat_agent.agent import root_agent
from app.core.config import settings
APP_NAME = settings.app_name

# These stay alive while the FastAPI process runs.
session_service = DatabaseSessionService(
    db_url=settings.database_url,
)
runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service,
)

async def chat(
    *,
    user_id: str,
    message: str,
    session_id: str | None = None,
) -> tuple[str, str]:
    """Run one chat turn and return (session_id, reply)."""

    if session_id is None or session_id =="":
        session = await session_service.create_session(
            app_name=APP_NAME,
            user_id=user_id,
        )
        session_id = session.id
    else:
        session = await session_service.get_session(
            app_name=APP_NAME,
            user_id=user_id,
            session_id=session_id,
        )
        if session is None:
            raise ValueError("Chat session not found")

    content = types.Content(
        role="user",
        parts=[types.Part.from_text(text=message)],
    )

    reply_parts: list[str] = []

    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=content,
    ):
        if event.is_final_response() and event.content:
            reply_parts.extend(
                part.text
                for part in event.content.parts or []
                if part.text
            )

    return session_id, "".join(reply_parts)