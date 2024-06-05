import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed


async def fetch_status(session: ClientSession,
                       url: str,
                       delay: int = 0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, 'https://example.com', 1),
                    fetch_status(session, 'https://example.com', 1),
                    fetch_status(session, 'https://example.com', 10)]
    
        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                print(await done_task)
            except asyncio.TimeoutError:
                print('Произошел тайм-аут!')

        for task in asyncio.tasks.all_tasks():
            print(task)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

            