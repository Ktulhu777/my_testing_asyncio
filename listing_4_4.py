import asyncio
import aiohttp
from util import fetch_status, async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://example.com'
        requests = [fetch_status(session, url) for _ in range(1_000)]
        status_code = await asyncio.gather(*requests)
        print("Success" if all(map(lambda code: code == 200, status_code)) else "Не все запросы выполнились")


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())