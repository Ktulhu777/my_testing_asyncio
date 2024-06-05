import asyncio
from util import async_timed
from aiohttp import ClientSession
from util import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        url = 'https://www.example.com'
        lst = [fetch_status(session, url) for _ in range(1)]
        status = await asyncio.gather(*lst)
        print(f'Состояние для {url} было равно {len(status)}', end=' | ')
        print("Все запросы выполнились" if all(map(lambda x: x == 200, status)) else "Не все запросы выполнились")
        # print(status)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
