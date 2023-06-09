"""тестова версія використання бібліотеки python-telegram-bot для взаємодії 
з Telegram API та бібліотеку requests для отримання даних з сайту."""
import config
import logging
import telegram
import requests
from dotenv import load_dotenv
 

load_dotenv()
#задаем уровень логов
logging.basicConfig(level=logging.INFO)

# Підключаємося до Telegram API
bot =  telegram.Bot(token='BOT_TOKEN')
wak = YOUR_API_KEY
print(bot)

# Функція для отримання прогнозу погоди
def get_weather(city):
    """Відправляємо запит до сервера та отримуємо результат у форматі JSON"""
    
    # Адреса для запиту до API
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={wak}&units=metric'
    # Отримуємо дані
    response = requests.get(url).json()

    # Перевіряємо, чи є дані про погоду в результаті запиту
    if 'weather' in response:
        # Отримуємо опис погоди та температуру
        weather_description = response['weather'][0]['description']
        temperature = response['main']['temp']
        # Формуємо повідомлення з прогнозом погоди
        message = f"Погода в місті {city}: {weather_description}. Температура: {temperature}°C."
    else:
        message = "На жаль, не вдалося отримати прогноз погоди для цього міста."

    return message


#Функція для обробки повідомлень від користувачів
def handle_message(update, context):
    # Отримуємо повідомлення від користувача
    message = update.message.text
    # Отримуємо ім'я користувача
    username = update.message.from_user.first_name
    # Якщо користувач відправив команду /start, вітаємо його
    if message == '/start':
        bot.send_message(chat_id=update.effective_chat.id, text=f"Привіт, {username}! Я допоможу тобі дізнатися прогноз погоди. Просто введи назву міста.")
    else:
        # Інакше, отримуємо прогноз погоди для введеного міста
        weather = get_weather(message)
        # Відправляємо повідомлення з прогнозом погоди користувачеві
        bot.send_message(chat_id=update.effective_chat.id, text=weather)
    #Створюємо обробник повідомлень
    dispatcher = telegram.ext.Dispatcher(bot, None)
    dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

    #Запускаємо чат-бота
    updater = telegram.ext.Updater('BOT_TOKEN', use_context=True)
    updater.dispatcher = dispatcher
    updater.start_polling()
    updater.idle()