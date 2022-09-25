from aiogram.utils import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os
from dotenv import load_dotenv  # pip install python-dotenv


async def __on_start_up(dp: Dispatcher) -> None:
    ...


def start_bot():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'), parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
