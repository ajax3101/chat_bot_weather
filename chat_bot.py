import telegram
import requests

# Отримуємо API ключ бота
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# Підключаємося до Telegram API
bot = telegram.Bot(token=BOT_TOKEN)

# Функція для отримання прогнозу погоди
def get_weather(city):
    # Адреса для запиту до API
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric'
    # Отримуємо дані