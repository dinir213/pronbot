from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from create_bot import admin_id
async def create_admin_kb(language, user_id):
    text0 = {
        'ru': "Общая статистика",
        'en': "General statistics",
        'de': "Allgemeine Statistiken",
        'es': "Estadísticas generales",
        'pt': "Estatísticas gerais",
        'iw': "סטטיסטיקה כללית",
        'zh': "一般统计数字",
        'fr': "Statistiques générales",
        'it': "Statistiche generali"
    }
    text1 = {
        'ru': "Статистика реферала",
        'en': "Referral Statistics",
        'de': "Empfehlungsstatistiken",
        'es': "Estadísticas de referencia",
        'pt': "Estatísticas de referência",
        'iw': "סטטיסטיקה של הפניות",
        'zh': "转介统计数字",
        'fr': "Statistiques de référence",
        'it': "Statistiche di riferimento"
    }
    text2 = {
        'ru': "Добавление реферала",
        'en': "Add a referral",
        'de': "Hinzufügen einer Empfehlung",
        'es': "Agregar una referencia",
        'pt': "Adicionar uma referência",
        'iw': "הוספת הפניה",
        'zh': "添加推荐",
        'fr': "Ajout d'une référence",
        'it': "Aggiunta di un referral"
    }
    text3 = {
        'ru': "Удаление реферала",
        'en': "Delete a referral",
        'de': "Entfernen einer Empfehlung",
        'es': "Eliminar una referencia",
        'pt': "Remoção de referência",
        'iw': "הסרת הפניה",
        'zh': "删除引用",
        'fr': "Suppression d'une référence",
        'it': "Rimozione del referral"
    }
    if user_id == admin_id:
        return InlineKeyboardMarkup(row_width=2).add(
            types.InlineKeyboardButton(text=text0[language], callback_data='statistic_common'),
            types.InlineKeyboardButton(text=text1[language], callback_data='statistic_single'),
            types.InlineKeyboardButton(text=text2[language], callback_data='add_referer'),
            types.InlineKeyboardButton(text=text3[language], callback_data='delete_referer')
        )
    else:
        return InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton(text=text1[language], callback_data='statistic_single')
        )
async def create_admin_back_menu_kb(language):
    text_back = {
        'ru': "Назад",
        'en': "Back",
        'de': "Zurück",
        'es': "Atrás",
        'pt': "Atrás",
        'iw': "חזרה",
        'zh': "返回",
        'fr': "En arrière",
        'it': "Fa"
    }
    return InlineKeyboardMarkup().add(types.InlineKeyboardButton(text=text_back[language], callback_data='admin'))