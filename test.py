from telethon import TelegramClient
from telethon import functions

api_id = 14834490
api_hash = "b392250f1c7031238f11620f75f6707b"

client = TelegramClient("name", api_id, api_hash)


async def main():
    await client.start()

    query = "спартак"
    result = await client(functions.contacts.SearchRequest(
        q=query,
        limit=10
    ))
    print(result.stringify())

with client:
    client.loop.run_until_complete(main())
