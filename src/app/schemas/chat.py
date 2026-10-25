from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_id: str
    session_id: str
    message: str

class ChatResponse(BaseModel):
    session_id: str
    reply: str

class ChatHistoryResponse(BaseModel):
    session_id: str
    messages: list

class ChatHistoryRequest(BaseModel):
    user_id: str
    session_id: str

class ChatSessionsRequest(BaseModel):
    user_id: str

class ChatSessionsResponse(BaseModel):
    user_id: str
    sessions: list