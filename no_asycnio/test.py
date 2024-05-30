from asyncio import Future
import asyncio

counter = False

async def hello():
    global counter
    count = 0
    while not counter:
        await asyncio.sleep(1)
        count += 1
        print(f"ПОКА НЕТ ОБЪЕКТА. Прошло {count} c.")

def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future


async def set_future_value(future: Future) -> None:
    global counter
    await input("Что то")
    future.set_result(42)
    counter = True


async def main() -> None:
    future = make_request()
    print(f'Будущий объект готов? {future.done()}')
    await hello()
    value = await future
    print(f'Будущий объект готов? {future.done()}')
    print(value)


asyncio.run(main())