
import asyncio

async def hello():
    while True:
        print('hello')
        await asyncio.sleep(1)
async def main():
    try:
        await asyncio.wait_for(hello(), 5)
    except Exception:
        print('Whoa time out buddy')
        input()
asyncio.run(main())
print('goodbye')
input()