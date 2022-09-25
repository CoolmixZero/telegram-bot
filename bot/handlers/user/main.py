from aiogram import Bot, Dispatcher
from aiogram.types import Message


async def __start(message: Message) -> None:
    bot: Bot = message.bot
    chat_id = message.chat.id
    await bot.send_message(chat_id, f"Дарова <b>{message.from_user.first_name}</b>")


async def __help(message: Message) -> None:
    bot: Bot = message.bot
    await bot.send_message(message.chat.id, "ЗАЧЕМ ТЕБЕ НУЖНА ПОМОЩЬ?1!7")


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(__start, commands=["start"])
    dp.register_message_handler(__help, commands=['help'])
