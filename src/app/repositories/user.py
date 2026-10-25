# src/app/repositories/user.py

from sqlalchemy import or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.user import User


class UserRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_by_user_id(self, user_id: str) -> User | None:
        result = await self.db.execute(
            select(User).where(User.user_id == user_id)
        )
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> User | None:
        result = await self.db.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def get_by_login(self, login: str) -> User | None:
        result = await self.db.execute(
            select(User).where(
                or_(User.user_id == login, User.email == login.lower())
            )
        )
        return result.scalar_one_or_none()

    async def create(
        self,
        *,
        user_id: str,
        first_name: str,
        last_name: str,
        email: str,
        hashed_password: str,
    ) -> User:
        user = User(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            email=email.lower(),
            hashed_password=hashed_password,
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user