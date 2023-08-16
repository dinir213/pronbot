import time

from aiogram import types, Dispatcher
from keyboards.admin_kb import create_admin_kb
from aiogram.dispatcher import filters
from database.profile_db import get_count_all_profiles, get_count_profiles_in_24hours, get_count_clicks_on_1_btn, get_count_clicks_on_2_btn, get_count_profiles_for_referer, get_count_clicks_on_1_or_2_btn_for_referer, get_referer_code
async def admin_panel(message: types.Message):
    await message.answer('Выберите действие: ', reply_markup=(await create_admin_kb()))

async def view_statistic(call: types.CallbackQuery):
    if call.data.split('_')[1] == 'common':
        count_all_users = await get_count_all_profiles()
        count_users_in_24hours = await get_count_profiles_in_24hours()
        count_clicks_on_1_btn = await get_count_clicks_on_1_btn()
        count_clicks_on_2_btn = await get_count_clicks_on_2_btn()
        msg = f'Всего пользователей: {count_all_users}\nПользователей, зарегистрировавшихся в последние 24 часа: {count_users_in_24hours}\nПользователей, нажавших на 1-ую кнопку: {count_clicks_on_1_btn}\nПользователей, нажавших на 2-ую кнопку: {count_clicks_on_2_btn}'
        await call.message.edit_text(msg)
    elif call.data.split('_')[1] == 'single':
        referer_code = await get_referer_code(call.from_user.id)
        count_start_users = await get_count_profiles_for_referer(referer_code)
        count_click_1_btn_users = await get_count_clicks_on_1_or_2_btn_for_referer('click_on_1_button', referer_code)
        count_click_2_btn_users = await get_count_clicks_on_1_or_2_btn_for_referer('click_on_2_button', referer_code)
        msg = f'Всего пользователей: {count_start_users}\nПользователей, нажавших на 1-ую кнопку: {count_click_1_btn_users}\nПользователей, нажавших на 2-ую кнопку: {count_click_2_btn_users}'
        await call.message.edit_text(msg)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(admin_panel, filters.IDFilter(user_id=(701401228)), commands=['admin'])
    dp.register_callback_query_handler(view_statistic, text_startswith=['statistic_'])