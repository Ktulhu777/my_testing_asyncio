# Обработка всех результатов по мере поступления

import aiohttp
import asyncio
from util import fetch_status, async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        pending = [asyncio.create_task(fetch_status(session, url)) for _ in range(100)]

    while pending:
        try:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

            print(f'Число завершившихся задач: {len(done)}')
            print(f'Число ожидающих задач: {len(pending)}')

            for done_task in done:
                print(await done_task)
        except RuntimeError:
            print("Возникла ошибка")
            continue

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
