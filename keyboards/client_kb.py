from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
async def transl_buttons1(language):
    buttons = {
        'ru': "Интересно!",
        'en': "Interesting!",
        'de': "Interessant!",
        'es': "¡Interesante!",
        'pt': "Interessante!",
        'iw': "מעניין!",
        'zh': "有趣！",
        'fr': "Intéressant!",
        'it': "Interessante!"
    }
    return buttons[language]
async def transl_buttons2(language):
    buttons = {
        'ru': "Посмотреть",
        'en': "Watch",
        'de': "Ansehen",
        'es': "Ver",
        'pt': "Olhar",
        'iw': "מבט",
        'zh': "手表",
        'fr': "Regarder",
        'it': "Vedere"
    }
    return buttons[language]
async def create_first_kb(language):
    return InlineKeyboardMarkup().add(InlineKeyboardButton(text=(await transl_buttons1(language)), callback_data='view_second_text'))
async def create_second_kb(language):
    return InlineKeyboardMarkup().add(InlineKeyboardButton(text=(await transl_buttons2(language)), callback_data='view_third_text'))
async def create_third_kb(language):
    return InlineKeyboardMarkup().add(InlineKeyboardButton(text=(await transl_buttons2(language)), url='https://www.studionrx.com'))