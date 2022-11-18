import asyncio

from pyrogram import Client

print("Enter your app information from my.telegram.org/apps below.")


async def main():
    async with Client(
        ":memory:", api_id=int(input("API ID:","24475665")), api_hash=input("API HASH:","5870592958:AAG-Q0B8kdSLJ5dWVkms8Wkt6Es5shpJEJU")
    ) as app:
        print(await app.export_session_string())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
