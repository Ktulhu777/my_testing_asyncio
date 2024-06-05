import asyncio
from aiohttp import ClientSession
from util import fetch_status, async_timed


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        fetchers = \
            [asyncio.create_task(fetch_status(session, 'https://example.com')) for _ in range(100)]

        done, pending = await asyncio.wait(fetchers)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            result = await done_task
            print(result)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
