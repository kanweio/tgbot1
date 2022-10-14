from os import name
from unittest.mock import call

from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import logging


@dp.message_handler(commands=['mem'])
async def mem_command(message: types.Message):
    mem_photo = open("media/meme.jpg", "rb")
    await bot.send_photo(message.chat.id, mem_photo)


@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}!")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Как зовут кота в мультсериале про кота и мышь?"
    answers = [
        "Джерри",
        "Барсик",
        "Гав-гав",
        "Том",
        "Малыш"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        open_period=5,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    # markup = InlineKeyboardMarkup()
    # button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    # markup.add(button_call_1)
    question = "Какая порода котов лысая?"
    answers = [
        "сиамская",
        "сфинкс",
        "тайская",
        "корниш-рекс",
    ]
    photo = open("media/coraline.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=10,
    )


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await message.answer(int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)


if name == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
