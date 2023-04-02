# Telegram bot прогноза погоди
[![Python Version](https://img.shields.io/badge/python-3.11-brightgreen.svg)](https://python.org)

Простий Telegram бот на Python за допомогою aiogram бібліотеки. 
Працюємо з API погоди сервісу openweather та бібліотекою requests. 
Парсим JSON дані.

![Chat Weather Telegram Bot ](/chat_weather_bot.png)

Клонуємо репо

``` bash
git clone https://github.com/ajax3101/chat_bot_weather.git
````

Встановлюємо та активуємо віртуальне оточення
``` bash
     python3 -m venv venv
     . venv/bin/activate
  ````

Встановлюємо необхідні модулі для роботи:
Завантажуємо файл із залежностями проекту
``` bash
pip install -r requirements.txt
````
Запуск програми
``` bash
python tg_bot.py
````
**Увага!**
Необхідно створити config.py файл та ввести в нього токени сайтів openweathermap.org та telegram
Наприклад:
``` bash
# Отримуємо API ключ бота
BOT_TOKEN='1234567890:BBBGGHHF3A9raB_mcT5E8lsJkdsfjkwejkrj'
# Адреса для запиту до API https://api.openweathermap.org/
WEATHER_API_KEY='1234567890a0b875a34435343957def6ce7454'
````
Файл config.py повинен бути вказаний у файлі .gitignore щоб ваші налаштування не відлетіли в репозиторій