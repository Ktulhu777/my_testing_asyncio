# РАБОТАЕТ В СИСТЕМАХ UNIX

import asyncio, signal
from asyncio import AbstractEventLoop
from typing import Set

from util import delay


def cancel_tasks():
    print('Получен сигнал SIGINT!')
    tasks: Set[asyncio.Task] = asyncio.all_tasks()


async def main():
    loop: AbstractEventLoop = asyncio.get_event_loop()

    loop.add_signal_handler(sig=signal.SIGINT, callback=cancel_tasks)

    await delay(10)


if __name__ == "__main__":
    asyncio.run(main=main())