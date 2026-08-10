import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("Переменная окружения BOT_TOKEN не задана")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("botinfo"))
async def cmd_botinfo(message: Message):
    me = await bot.get_me() 

    await message.answer(
        "Информация о боте:\n" # С помощью \n мы делаем перенос строк
        f"ID: {me.id}\n" # Здесь выводим ID
        f"Имя: {me.first_name}\n" # Здесь first_name (ИмяБота)
        f"Username: @{me.username}" # Здесь username (@qwe123p1oi098_bot)
    )

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Напиши /botinfo")

@dp.message(F.text)
async def echo_message(message: Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())