from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp


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


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text=['button_1'])
    dp.register_callback_query_handler(quiz_3, text=['button_2'])
    dp.register_callback_query_handler(quiz_4, text=['button_3'])
