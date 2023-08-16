from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

async def create_first_kb():
    return InlineKeyboardMarkup().add(InlineKeyboardButton(text='Интересно!', callback_data='view_second_text'))
async def create_second_kb():
    return InlineKeyboardMarkup().add(InlineKeyboardButton(text='Посмотреть', callback_data='view_third_text'))