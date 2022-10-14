from aiogram import Bot, Dispatcher
from decouple import config
import telebot
t0ken = config("TOKEN")
bot = Bot(t0ken)
dp = Dispatcher(bot=bot)
