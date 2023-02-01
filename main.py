# 01.02.2023
from aiogram import types, executor
from module.cars_command import show_cars
from module.base import init, create_table
from config import dp


async def startup(_):
    """
        Функция для запуска сторонних сервисов
    """
    init()
    create_table()


#Регистор для машина_кг
dp.register_message_handler(show_cars, commands=['cars'])


#Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=startup)