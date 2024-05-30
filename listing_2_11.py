import asyncio
from util import delay

async def main():
    long_task = asyncio.create_task(delay(10))

    seconds = 0

    while not long_task.done():
        print('Задача не закончилась, следующая проверка через секунду.')
        await asyncio.sleep(1)
        seconds += 1
        if seconds == 5:
            long_task.cancel()

    try:
        await long_task
    except asyncio.CancelledError:
        print('Задача была снята')


asyncio.run(main())