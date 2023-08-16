from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

async def create_admin_kb():
    return InlineKeyboardMarkup(row_width=2).add(
        types.InlineKeyboardButton(text='Общая статистика', callback_data='statistic_common'),
        types.InlineKeyboardButton(text='Cтатистика реферала', callback_data='statistic_single'),
        types.InlineKeyboardButton(text='Добавление реферала', callback_data='add_referer')
    )