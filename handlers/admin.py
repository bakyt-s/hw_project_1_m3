from aiogram import types, Dispatcher
from config import bot, ADMINS
from random import choice


async def game(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINS:
            await message.answer('Actions prohibited!')
    else:
        emoji_list = ['⚽️', '🏀', '🎲', '🎯', '🎳', '🎰']
        random_emoji = choice(emoji_list)
        if message.text == 'game':
            return await message.answer_dice(emoji=random_emoji)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(game, commands=['game'])
