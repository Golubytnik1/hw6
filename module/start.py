from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

""" Обработчик категорий """
start_kb = InlineKeyboardMarkup(resize_keyboard=True)
start_kb.add(InlineKeyboardButton('Список машин', callback_data='cars'))


async def start_command(message: types.Message):
	"""
        Функция приветствия пользователя
	"""
	await message.answer(text="Приветствую вас уважаемый!", reply_markup=start_kb)
	await message.delete()