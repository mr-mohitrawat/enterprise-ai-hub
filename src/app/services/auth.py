# src/app/services/auth.py

from fastapi import HTTPException, status
from pwdlib import PasswordHash
from sqlalchemy.exc import IntegrityError

from app.core.security import create_access_token
from app.repositories.user import UserRepository
from app.schemas.auth import (
    LoginRequest,
    SignupRequest,
    TokenResponse,
    UserResponse,
)

password_hash = PasswordHash.recommended()


async def signup(db, request: SignupRequest) -> UserResponse:
    repo = UserRepository(db)

    if await repo.get_by_user_id(request.user_id):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User ID is already taken",
        )

    normalized_email = request.email.strip().lower()
    if await repo.get_by_email(normalized_email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email is already registered",
        )

    try:
        user = await repo.create(
            user_id=request.user_id,
            first_name=request.first_name.strip(),
            last_name=request.last_name.strip(),
            email=normalized_email,
            hashed_password=password_hash.hash(request.password),
        )
    except IntegrityError:
        # The database unique constraints also protect against concurrent signups.
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User ID or email is already registered",
        )

    return UserResponse(
        user_id=user.user_id,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
    )


async def login(db, request: LoginRequest) -> TokenResponse:
    repo = UserRepository(db)
    user = await repo.get_by_login(request.login.strip())

    if user is None or not password_hash.verify(
        request.password,
        user.hashed_password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user ID/email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return TokenResponse(
        access_token=create_access_token(user.user_id),
        token_type="bearer",
    )