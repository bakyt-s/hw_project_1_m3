from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import logging

TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f'Hello Master - {message.from_user.first_name}!\n'
        f'You can use the following Bot options:\n'
        f'/quiz - star the QUIZ\n'
        f'/help - correct answers to the QUIZ questions\n'
        f'/meme - get a meme picture'
    )


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f'study again Python lesson 1'
    )


@dp.message_handler(commands=['quiz'])
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


@dp.callback_query_handler(text='button_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton('Next ->', callback_data='button_2')
    markup.add(button_2)

    question_2 = 'Which of these collections defines a TUPLE?'
    answers_2 = [
        "['Python', 'C', 'Java']",
        "('Python', 'C', 'Java')",
        "{'language': 'Python', 'paradigm': 'OOP'}",
        "{'Python', 'C', 'Java'}"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question_2,
        options=answers_2,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='from Python lesson 1',
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(text='button_2')
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_3 = InlineKeyboardButton('Next ->', callback_data='button_3')
    markup.add(button_3)

    question_3 = 'Which of these collections defines a SET?'
    answers_3 = [
        "['Python', 'C', 'Java']",
        "('Python', 'C', 'Java')",
        "{'language': 'Python', 'paradigm': 'OOP'}",
        "{'Python', 'C', 'Java'}"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question_3,
        options=answers_3,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='from Python lesson 1',
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(text='button_3')
async def quiz_4(call: types.CallbackQuery):
    question_4 = 'Which of these collections defines a DICTIONARY?'
    answers_4 = [
        "['Python', 'C', 'Java']",
        "('Python', 'C', 'Java')",
        "{'language': 'Python', 'paradigm': 'OOP'}",
        "{'Python', 'C', 'Java'}"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question_4,
        options=answers_4,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='from Python lesson 1',
        open_period=10
    )

    await bot.send_message(chat_id=call.from_user.id, text='End of the QUIZ!')


@dp.message_handler(commands=['meme'])
async def send_meme(message: types.Message):
    await bot.send_photo(message.from_user.id, 'https://urlme.me/success/typed_a_url/made_a_meme.jpg')


@dp.message_handler()
async def bot_echo(message: types.Message):
    if message.text.isdigit():
        message.text = int(message.text)
        return await bot.send_message(message.from_user.id, f'{message.text ** 2}')
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
