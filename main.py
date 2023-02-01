# 01.02.2023
from aiogram import executor
from module.command import cars_list
from module.base import create_table, init
from config import dp


async def startup(_):
    init()
    create_table()


dp.register_message_handler(cars_list, commands=['cars'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=startup)