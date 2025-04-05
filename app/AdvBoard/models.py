"""
This module with models, which will be used in views.
"""

from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from sqlalchemy import String, DateTime, func, ForeignKey


class Base(DeclarativeBase, AsyncAttrs):
    """Base class for models."""
    __abstract__ = True


class User(Base):
    """Model for user table."""
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False)

    advertisements: Mapped[list["Advertisement"]] = relationship("Advertisement", back_populates="owner", cascade="all, delete-orphan")

    @property
    def dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Advertisement(Base):
    """Model for advertisement table."""
    __tablename__ = 'advertisements'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(200), nullable=False)
    creation_date: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner: Mapped[User] = relationship("User", back_populates="advertisements")

    @property
    def dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "creation_date": self.creation_date.strftime("%B %d, %Y"),
            "owner": self.user_id
        }