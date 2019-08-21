from time import sleep
import asyncio
import requests


async def foo():
    return 'foo'


def main():
    await foo()

main()