from time import sleep
from aiogram import types
from module.base import done_cars


async def show_cars(message: types.Message):
    """
        Функция покажет пользователю команды
    """
    i = 0
    for i in range(len(done_cars())):
        car = done_cars()[i]

        await message.answer(text=f'''
Марка - {car[1]} 
Цена - {car[2]}
Ссылка - {car[3]}
''')
        sleep(3)
    await message.delete()