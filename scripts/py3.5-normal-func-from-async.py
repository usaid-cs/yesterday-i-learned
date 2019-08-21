from time import sleep
import asyncio
import requests


def foo():
    return 'foo'


async def main():
    print(foo())

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()