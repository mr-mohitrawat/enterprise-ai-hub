# src/app/schemas/auth.py

from pydantic import BaseModel, EmailStr, Field


class SignupRequest(BaseModel):
    user_id: str = Field(min_length=3, max_length=50)
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(min_length=12, max_length=128)


class LoginRequest(BaseModel):
    # Accept either the user's unique ID or email.
    login: str
    password: str


class UserResponse(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    email: EmailStr


class TokenResponse(BaseModel):
    access_token: str
    token_type: str