from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp


async def start_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f'Hello Master - {message.from_user.first_name}!\n'
        f'You can use the following Bot options:\n'
        f'/quiz - star the QUIZ\n'
        f'/help - correct answers to the QUIZ questions\n'
        f'/meme1 or /meme2- get a meme picture'
    )


async def help_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f'study again Python lesson 1'
    )


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('Next ->', callback_data='button_1')
    markup.add(button_1)

    question_1 = 'Which of these collections defines a LIST?'
    answers_1 = [
        "['Python', 'C', 'Java']",
        "('Python', 'C', 'Java')",
        "{'language': 'Python', 'paradigm': 'OOP'}",
        "{'Python', 'C', 'Java'}"
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question_1,
        options=answers_1,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='from Python lesson 1',
        open_period=10,
        reply_markup=markup
    )


async def send_meme_1(message: types.Message):
    await bot.send_photo(message.from_user.id, 'https://urlme.me/success/typed_a_url/made_a_meme.jpg')


async def send_meme_2(message: types.Message):
    photo = open('media/meme.jpeg', 'rb')
    await bot.send_photo(message.from_user.id, photo)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(send_meme_1, commands=['meme1'])
    dp.register_message_handler(send_meme_2, commands=['meme2'])
