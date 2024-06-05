import asyncio, threading
from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


async def main() -> None:
    url: str = 'https://example.com'
    async with ClientSession() as session:
        calls = [fetch_status(session=session, url=url) for _ in range(25)]
        result = await asyncio.gather(*calls)
        print(result)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

thread = threading.Thread(target=asyncio.run(main()))
thread_2 = threading.Thread(target=asyncio.run(main()))

thread.start()
thread_2.start()

thread.join()
thread_2.join()
