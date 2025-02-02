import requests


def weather(place):
    url = 'https://wttr.in/{}?nTqmM&lang=ru'.format(place)
    responce = requests.get(url)
    responce.raise_for_status()
    return print(responce.text)


def main():
    city_lst = ['Лондон', 'Шереметьево', 'Череповец']
    for city in city_lst:
        weather(city)


if __name__ == "__main__":
    main()
