"""У цьому коді ми спочатку підключаємося до Telegram API за допомогою токена бота. Далі ми створюємо функцію `get_weather`, 
яка отримує назву міста та повертає прогноз погоди для цього міста з сайту https://openweathermap.org/. 
Функція `handle_message` обробляє повідомлення від користувачі
Ключі (Token API) від telegram та openweathermap.org знаходиться у налаштуваннях файлу .env"""
import requests
import datetime
from config import WEATHER_API_KEY as wak, BOT_TOKEN as bt
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


# инициализируем бота
bot = Bot(token=bt)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привіт! Я допоможу тобі дізнатися прогноз погоди. Просто введи назву міста.")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        # Адреса для запиту до API
        url = f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={wak}&units=metric&lang=ua'
        # Отримуємо дані
        response = requests.get(url).json()

        city = response["name"]
        temp = response["main"]["temp"]
        humidity = response["main"]["humidity"]
        pressure = response["main"]["pressure"]
        wind = response["wind"]["speed"]
        weather = response["weather"][0]["description"]
        sunrise = datetime.datetime.fromtimestamp(response["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(response["sys"]["sunset"])
        light_day = datetime.datetime.fromtimestamp(
            response["sys"]["sunset"]) - datetime.datetime.fromtimestamp(response["sys"]["sunrise"])
        await message.reply(f"-=-{datetime.datetime.now().strftime('%H:%M, %d/%m/%Y')}-=-\n"
                            f"Погода в місті: {city}.\n Температура: {temp}° C.\n"
                            f" Вологість: {humidity}%\n Тиск: {pressure} мм.рт.ст.\n Вітер: {wind} м/х\n"
                            f" Схід сонця: {sunrise}\n Захід сонця: {sunset}.\n"
                            f" Тривалість дня: {light_day}\n"
                            f" Тип погоди: {weather}"
                            )

    except:
        await message.reply('\U0001F645 На жаль, не вдалося отримати прогноз погоди для цього міста. \U0001F645')

if __name__ == '__main__':
    executor.start_polling(dp)
