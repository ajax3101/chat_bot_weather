import requests
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
        pprint(response)
        
    except Exception as ex:
        print(ex)
        print('На жаль, не вдалося отримати прогноз погоди для цього міста.')



def main():
    city = input('Введи назву міста: ')
    get_weather(city, wak)


if __name__ == '__main__':
    main()
