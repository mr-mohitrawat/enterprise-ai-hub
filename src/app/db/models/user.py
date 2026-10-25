# src/app/db/models/user.py

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    # Public, user-chosen identifier used for login.
    user_id: Mapped[str] = mapped_column(
        String(50),
        primary_key=True,
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    # Store normalized lowercase email in the service/repository.
    email: Mapped[str] = mapped_column(
        String(320),
        unique=True,
        index=True,
        nullable=False,
    )

    # Store only the Argon2 hash, never the raw password.
    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )