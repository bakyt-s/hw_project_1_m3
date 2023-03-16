from aiogram import types, Dispatcher
from config import bot


async def pin(message: types.Message):
    if message.text.startswith('!pin'):
        await message.pin()


async def bot_echo(message: types.Message):
    if message.text.isdigit():
        message.text = int(message.text)
        return await bot.send_message(message.from_user.id, f'{message.text ** 2}')
    else:
        await bot.send_message(message.from_user.id, message.text)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix="!/")
    dp.register_message_handler(bot_echo)
