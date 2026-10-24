from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_id: str
    session_id: str
    message: str

class ChatResponse(BaseModel):
    session_id: str
    reply: str