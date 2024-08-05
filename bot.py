from aiogram import Bot, Dispatcher
from asyncio import run
from consts import BOT_TOKEN
import logging
import message
import callback_data
import data

dp = Dispatcher()

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(BOT_TOKEN)
    dp.include_router(message.router)
    dp.include_router(callback_data.router)
    
    data.default_requests()
    await dp.start_polling(bot)
    data.close_db()

run(main())