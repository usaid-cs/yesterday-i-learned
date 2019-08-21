from time import sleep
import asyncio
import requests


async def foo():
    print("foo start")
    requests.get('https://i.imgur.com/jdxrKeq.mp4')
    print("foo end")


async def main():
    print("main start")
    a = foo()
    print("foo running")
    asyncio.sleep(1)
    await a
    print("main end")


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()