# 01.02.2023
from aiogram import executor
from module.base import init, create_table, done_cars
from module.cars_parser import get_cars
from module.start import start_command
from config import dp


async def startup(_):
    """
        Функция для запуска сторонних сервисов
    """
    init()
    create_table()
    done_cars()


#Запуск бота
if __name__ == '__main__':
    # Регистор для машина_кг
    dp.register_message_handler(get_cars, commands=['cars'])
    # Регистор для старта
    dp.register_message_handler(start_command, commands=['start'])

    executor.start_polling(dp, skip_updates=True, on_startup=startup)