"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from datetime import datetime
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Text
)
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

from sqlalchemy.orm import declarative_base, declared_attr, relationship, sessionmaker

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

# PG_CONN_URI = "postgresql+asyncpg://username:passwd!@localhost:5432/blog"

DB_ECHO = True


async_engine: AsyncEngine = create_async_engine(
    PG_CONN_URI, echo=DB_ECHO
)


async_session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


Base = declarative_base(cls=Base)


class TimestampMixin:
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())


class User(TimestampMixin, Base):
    name = Column(String(200), unique=False)
    username = Column(String(200), unique=True)
    email = Column(String(200), unique=True)

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return (
            f"{self.__class__.__name__}"
            f"(id={self.id}, "
            f"name={self.name!r}, "
            f"username={self.username!r}, "
            f"e_mail={self.email})"
        )


class Post(TimestampMixin, Base):
    title = Column(String(500))
    body = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="post")

    def __str__(self):
        return (f"{self.__class__.__name__}"
                f"(id={self.id}, "
                f"title={self.title!r}, "
                f"body={self.body}), "
                f"user_id={self.user_id}"
                )



