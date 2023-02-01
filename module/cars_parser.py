import requests
from aiogram import types
from bs4 import BeautifulSoup as BS

URL = 'https://www.mashina.kg/search/all/'


async def get_cars(message: types.Message):
    global cars
    response = requests.get(URL)
    print(response)
    if response.status_code == 200:
        # print(response.text)
        soup = BS(response.text, 'html.parser')
        ads_table = soup.find('div', class_='table-view-list') # таблица с объявлениями
        ad_cards = ads_table.find_all('div', class_='list-item') # все карточки объявлений
        cars = []
        for c in ad_cards:
            car = {
                'title': c.find('h2', class_='name').string.replace('\n', '').strip(),
                'price': c.find('div', class_='price').find('strong').string.replace('\n', '').strip(),
                'link': f"https://mashina.kg{c.find('a').get('href').strip()}"
            }
            cars.append(car)

        print(cars)
    await message.answer(text='Вот ассартимент машин: \n'
                              f'{cars}')




if __name__ == "__main__":
    get_cars()