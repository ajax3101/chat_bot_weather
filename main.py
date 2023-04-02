import requests
import datetime
from config import WEATHER_API_KEY as wak
from pprint import pprint

# Функція для отримання прогнозу погоди


def get_weather(city, wak):
    """Відправляємо запит до сервера та отримуємо результат у форматі JSON"""
    try:
        # Адреса для запиту до API
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={wak}&units=metric&lang=ua'
        # Отримуємо дані
        response = requests.get(url).json()
        # print(type(response))
        # pprint(response)

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
        print(f"-=-{datetime.datetime.now().strftime('%H:%M, %d/%m/%Y')}-=-\n"
              f"Погода в місті: {city}.\n Температура: {temp}° C.\n"
              f" Вологість: {humidity}%\n Тиск: {pressure} мм.рт.ст.\n Вітер: {wind} м/х\n"
              f" Схід сонця: {sunrise}\n Захід сонця: {sunset}.\n"
              f" Тривалість дня: {light_day}\n"
              f" Погода: {weather}"
              )

    except Exception as ex:
        print(ex)
        print('На жаль, не вдалося отримати прогноз погоди для цього міста.')


def main():
    city = input("Введи назву міста: ")
    get_weather(city, wak)


if __name__ == '__main__':
    main()
