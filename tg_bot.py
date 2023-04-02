import requests
import datetime
from config import WEATHER_API_KEY as wak, BOT_TOKEN as bt
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


#инициализируем бота
bot = Bot(token=wak)
dp = Dispatcher(bot)