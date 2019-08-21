from time import sleep
import asyncio
import requests


async def foo():
    print("foo start")
    requests.get('https://i.imgur.com/jdxrKeq.mp4')
    print("foo end")



def async_root(fn):
    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(fn())
        finally:
            loop.close()
    return wrapper


@async_root
async def main():
    print("main start")
    a = foo()
    print("foo running")
    asyncio.sleep(1)
    await a
    print("main end")



main()