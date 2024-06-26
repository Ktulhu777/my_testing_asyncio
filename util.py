import asyncio
import functools
import time
from typing import Callable, Any

from aiohttp import ClientSession


async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')

    await asyncio.sleep(delay_seconds)

    print(f'сон в течение {delay_seconds} с закончился')

    return delay_seconds


async def add_one(number: int) -> int:
    return number + 1


async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'выполняется {func.__name__} с аргументами {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func} завершилась за {total:.4f} с')

        return wrapped

    return wrapper
