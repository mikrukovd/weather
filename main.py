import requests


def get_weather(city):
    params = {
        'nTqmM': '',
        'lang': 'ru'
    }
    url = 'https://wttr.in/{}'.format(city)
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def main():
    cities = ['Лондон', 'Шереметьево', 'Череповец']
    for city in cities:
        print(get_weather(city))


if __name__ == "__main__":
    main()
