import asyncio
import aiohttp
import json
from dataclasses import dataclass

from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_user_data():
    async with ClientSession() as session:
        url = USERS_DATA_URL

        async with session.get(url=USERS_DATA_URL) as responce:
            users_data = await responce.json()

            print(users_data)
            return users_data