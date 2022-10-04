"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio
import aiohttp
from dataclasses import dataclass

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


@dataclass(frozen=True)
class Service:
    url: str


SERVICES = [
    Service(url=USERS_DATA_URL),
    Service(url=POSTS_DATA_URL)
]


async def fetch_json(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        data = await response.json()
        return data


async def fetch_data(service: Service) -> str | None:

    async with aiohttp.ClientSession() as session:
        data: dict = await fetch_json(session, service.url)
        print(data)
        return data


async def get_users_posts() -> list[dict]:
    users_data: list[dict]
    post_data: list[dict]
    users_data, post_data = await asyncio.gather(
        fetch_data(SERVICES[0]),
        fetch_data(SERVICES[1]))
    return users_data, post_data



def main():
    asyncio.run(get_users_posts())
    # users_data = asyncio.run(fetch_data(SERVICES[0]))
    # post_data = asyncio.run(fetch_data(SERVICES[1]))
    # print(users_data)
    # return users_data, post_data


if __name__ == "__main__":
    main()