import logging
from aiogram import Bot, Dispatcher, executor, types
from telethon import TelegramClient
from telethon import functions
import asyncio
import nest_asyncio

bot = Bot(token="5128042454:AAENWMjPuNzQFwlnzvUiv6zYcyAi7MtG0qo")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
api_id = 14834490
api_hash = "b392250f1c7031238f11620f75f6707b"
result = None
nest_asyncio.apply()
# client = TelegramClient("name", api_id, api_hash)


async def register():
    global client
    client = TelegramClient("name", api_id, api_hash)
    await client.start()

# loop = asyncio.new_event_loop()
# loop.run_until_complete(register())
# print(9)
# loop.stop()
# loop.close()


async def search(query):
    try:
        global result
        # client = TelegramClient("name", api_id, api_hash)
        async with TelegramClient("name", api_id, api_hash) as client:
            await client.start()
            print(query)
            print(client)
            result = await client(functions.contacts.SearchRequest(
                q=query,
                limit=100
            ))
        result = list(result.to_dict()["chats"])
        await asyncio.sleep(.5)
    except Exception as e:
        print(2)
        print(e)
    finally:
        return


@dp.message_handler(commands="start")
async def introduction(message: types.Message):
    await message.answer("Здравствуйте. Введите ваш запрос и я отправлю вам все ссылки, которые найду")


@dp.message_handler()
async def main(message: types.Message):
    print(1)
    # код из api
    query = str(message.text)
    loop = asyncio.new_event_loop()
    loop.run_until_complete(search(query))
    loop.stop()
    loop.close()
    print(result)
    res = list(result)
    for link in res:
        await message.answer("https://t.me/" + link["username"])
    return


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
