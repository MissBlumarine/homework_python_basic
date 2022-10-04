"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from sqlalchemy.orm import sessionmaker, Session

import models
from models import User, Post, Base
from jsonplaceholder_requests import get_users_posts

async_engine: AsyncEngine = create_async_engine(
    models.PG_CONN_URI,
    echo=models.DB_ECHO,
)

async_session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def create_tables():
    async with async_engine.begin() as conn:
        print("todo: drop all")
        await conn.run_sync(models.Base.metadata.drop_all)
        print("todo: create all")
        await conn.run_sync(models.Base.metadata.create_all)

        print("created all")
        await conn.run_sync(models.Base.metadata.create_all)


async def create_user(session: AsyncSession, username: str, name: str, email: str) -> User:
    user = User(name=name, username=username, email=email)
    session.add(user)
    #await session.commit()
    print(user)

    return user


async def create_post(session: AsyncSession, user_id: int, title: str, body: str) -> Post:
    post = Post(user_id=user_id, title=title, body=body)
    session.add(post)
    #await session.commit()

    return post


async def run_create_tables(session: async_session):
    users_data, posts_data = await get_users_posts()
    async with async_session() as session:
        async with session.begin():
            for user in users_data:
                await create_user(
                    session,
                    user.get("name"),
                    user.get("username"),
                    user.get("email")
                )

            for post in posts_data:
                await create_post(
                    session,
                    post.get("userId"),
                    post.get("title"),
                    post.get("body")
                )
    await session.commit()


async def async_main():
    await create_tables()
    async with async_session() as session:
        await run_create_tables(session)
        
def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
