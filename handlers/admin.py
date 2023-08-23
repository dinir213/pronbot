from aiogram import types, Dispatcher
from create_bot import bot
from keyboards.admin_kb import create_admin_kb, create_admin_back_menu_kb
from database.profile_db import get_count_all_profiles, get_count_profiles_in_24hours, get_count_clicks_on_1_btn, get_count_clicks_on_2_btn, get_count_profiles_for_referer, get_count_clicks_on_1_or_2_btn_for_referer, get_referer_code, get_partner_user_ids, input_partner_user_ids, get_profile_language, get_partner_datas, del_partner_data, get_partner_referer_codes, get_all_users_db
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from create_bot import admin_id
from os import remove
class Referers(StatesGroup):
    referer_code = State()
    user_id = State()

async def msg_menu_no_cant(language):
    msg_menu_no_cant_text = {
        'ru': "Недостаточно прав",
        'en': "Not enough rights",
        'de': "Nicht genügend Rechte",
        'es': "No hay suficientes derechos",
        'pt': "Direitos insuficientes",
        'iw': "לא מספיק זכויות",
        'zh': "没有足够的权利",
        'fr': "Droits insuffisants",
        'it': "Diritti insufficienti"
    }
    return msg_menu_no_cant_text[language]
async def msg_menu(language):
    msg_admin_menu = {
        'ru': "Выберите действие:\n\n",
        'en': "Select an action\n\n",
        'de': "Aktion auswählen:\n\n",
        'es': "Seleccione una acción:\n\n",
        'pt': "Escolha uma ação:\n\n",
        'iw': "בחר פעולה:\n\n",
        'zh': "选择操作:\n\n",
        'fr': "Sélectionnez une action:\n\n",
        'it': "Seleziona azione:\n\n"
    }
    return msg_admin_menu[language]
async def msg_view_statistic_single(referer_code, count_start_users, count_click_1_btn_users, count_click_2_btn_users, language):
    msg_view_statistic_single = {
        'ru': f'Реферер: {referer_code}\n\nВсего пользователей: {count_start_users}\nПользователей, нажавших на 1-ую кнопку: {count_click_1_btn_users}\nПользователей, нажавших на 2-ую кнопку: {count_click_2_btn_users}\n',
        'en': f"Referrer: {referer_code}\n\nTotal users: {count_start_users}\nUsers who clicked on the 1st button: {count_click_1_btn_users}\nUsers who clicked on the 2nd button: {count_click_2_btn_users}\n",

        'de': f"Referrer: {referer_code}\n\nBenutzer insgesamt: {count_start_users}\nBenutzer, die auf die 1. Schaltfläche geklickt haben: {count_click_1_btn_users}\nBenutzer, die auf die 2. Schaltfläche geklickt haben: {count_click_2_btn_users}\n",
        'es': f"Referente: {referer_code}\n\nTotal de usuarios: {count_start_users}\nUsuarios que han pulsado el botón 1: {count_click_1_btn_users}\nUsuarios que han pulsado el segundo botón: {count_click_2_btn_users}\n",
        'pt': f"Referenciador: {referer_code}\n\nTotal de utilizadores: {count_start_users}\nUsuários que clicaram no botão 1: {count_click_1_btn_users}\nUsuários que clicaram no botão 2: {count_click_2_btn_users}\n",
        'iw': f'מפנה: \n{referer_code} \n\n סה " כ משתמשים: {count_start_users} \n\n משתמשים שלחצו על כפתור 1: {count_click_1_btn_users} \n\n משתמשים שלחצו על כפתור 2: {count_click_2_btn_users}',
        'zh': f"推荐人: {referer_code}\n\n用户总数: {count_start_users}\n点击第一个按钮的用户: {count_click_1_btn_users}\n点击第二个按钮的用户: {count_click_2_btn_users}\n",
        'fr': f"Référent: {referer_code}\n\nNombre total d'utilisateurs: {count_start_users}\nUtilisateurs ayant cliqué sur le 1er bouton: {count_click_1_btn_users}\nUtilisateurs qui ont cliqué sur le 2ème bouton: {count_click_2_btn_users}\n",
        'it': f"Referrer: {referer_code}\n\nTotale utenti: {count_start_users}\nUtenti che hanno fatto clic sul primo pulsante: {count_click_1_btn_users}\nUtenti che hanno fatto clic sul secondo pulsante: {count_click_2_btn_users}\n"
    }
    return msg_view_statistic_single[language]
async def msg_view_statistic_common(count_all_users, count_users_in_24hours, count_clicks_on_1_btn, count_clicks_on_2_btn, language):
    msg_view_statistic_common = {
        'ru': f"Всего пользователей: {count_all_users}\nПользователей, зарегистрировавшихся в последние 24 часа: {count_users_in_24hours}\nПользователей, нажавших на 1-ую кнопку: {count_clicks_on_1_btn}\nПользователей, нажавших на 2-ую кнопку: {count_clicks_on_2_btn}",
        'en': f"Total users: {count_all_users}\n Users who have registered in the last 24 hours: {count_users_in_24hours}\n Users who clicked on the 1st button: {count_clicks_on_1_btn}\n Users who clicked on the 2nd button: {count_clicks_on_2_btn}",
        'de': f"Benutzer insgesamt: {count_all_users}\nBenutzer, die sich in den letzten 24 Stunden angemeldet haben: {count_users_in_24hours}\nBenutzer, die auf die 1. Schaltfläche geklickt haben: {count_clicks_on_1_btn}\nBenutzer, die auf die 2. Schaltfläche geklickt haben: {count_clicks_on_2_btn}",
        'es': f"Total de usuarios: {count_all_users}\nUsuarios registrados en las últimas 24 horas: {count_users_in_24hours}\nUsuarios que hicieron clic en el primer botón: {count_clicks_on_1_btn} \ n Usuarios que hicieron clic en el segundo botón: {count_clicks_on_2_btn}",
        'pt': f"Total de utilizadores: {count_all_users}\nUtilizadores registados nas últimas 24 horas: {count_users_in_24hours}\nutilizadores que clicaram no botão 1: {count_clicks_on_1_btn}\nUtilizadores que clicaram no botão 2: {count_clicks_on_2_btn}",
        'iw': f'סה " כ משתמשים: {count_all_users} \n משתמשים שנרשמו ב-24 השעות האחרונות: {count_users_in_24hours}\n משתמשים שלחצו על כפתור 1: {count_clicks_on_1_btn}\n משתמשים שלחצו על כפתור 2: {count_clicks_on_2_btn}',
        'zh': f"总用户数：{count_all_users}\n最近24小时内注册的用户数：{count_users_in_24hours}\n点击第一个按钮的用户数：{count_clicks_on_1_btn}\n点击第二个按钮的用户数：{count_clicks_on_2_btn}",
        'fr': f"Nombre total d'utilisateurs: {count_all_users}\nUtilisateurs enregistrés au cours des 24 dernières heures: {count_users_in_24hours}\nUtilisateurs ayant cliqué sur le 1er bouton: {count_clicks_on_1_btn}\nUtilisateurs ayant cliqué sur le 2ème bouton: {count_clicks_on_2_btn}",
        'it': f"Utenti totali: {count_all_users}\nUtenti registrati nelle ultime 24 ore: {count_users_in_24hours}\nUtenti che hanno fatto clic sul primo pulsante: {count_clicks_on_1_btn}\nUtenti che hanno fatto clic sul secondo pulsante: {count_clicks_on_2_btn}"
    }
    return msg_view_statistic_common[language]
async def msg_referer_func(call, language):
    msg_referer_user_id = {
        'ru': f'Введите referer_code для добавления в систему, к примеру:\n\nbest.chanel',
        'en': "Enter the referral_code to add to the system, for example:\n\nbest.channel",
        'de': "Geben Sie referral_code ein, um es dem System hinzuzufügen, zum Beispiel:\n\nbest.channel",
        'es': "Escriba referral_code para agregar al sistema, por ejemplo:\n\nbest.channel",
        'pt': "Digite referral_code para adicionar ao sistema, por exemplo:\n\nbest.channel",
        'iw': "הקלד referral_code כדי להוסיף למערכת, למשל:\n \ best.channel",
        'zh': "输入要添加到系统的referral_code，例如：\n\nbest.channel",
        'fr': "Tapez referral_code à ajouter au système, par exemple:\n\nbest.channel",
        'it': "Digitare referral_code da aggiungere al sistema, ad esempio:\n\nbest.channel"
    }
    return msg_referer_user_id[language]
async def msg_create_referal_to_view(language):
    msg = {
    'ru': "Создайте реферала, чтобы смотреть статистику по каждому рефералу",
    'en': "Create a referral to view statistics for each referral",
    'de': "Erstellen Sie eine Empfehlung, um die Statistiken für jede Empfehlung zu sehen",
    'es': "Cree una referencia para ver las estadísticas de cada referencia",
    'pt': "Crie uma referência para ver as estatísticas de cada referência",
    'iw': "צור הפניה לצפייה בסטטיסטיקה עבור כל הפניה",
    'zh': "创建引用以查看每个引用的统计信息",
    'fr': "Créez une référence pour voir les statistiques sur chaque référence",
    'it': "Crea un referral per vedere le statistiche per ogni referral"
    }
    return msg[language]
async def msg_referer_referer_code_func(message, language):
    msg_referer_user_id = {
        'ru': f'Введите user_id партнера, к примеру: 701401228',
        'en': "Enter the partner's user_id, for example: 701401228",
        'de': "Geben Sie die user_id des Partners ein, zum Beispiel: 701401228",
        'es': "Introduzca el user_id del socio, por ejemplo: 701401228",
        'pt': "Digite user_id do parceiro, por exemplo: 701401228",
        'iw': "הזן את user_id של השותף, למשל: 701401228",
        'zh': "输入合作伙伴的user_id，例如：701401228",
        'fr': "Entrez l'user_id du partenaire, par exemple: 701401228",
        'it': "Immettere user_id del partner, ad esempio: 701401228"
    }
    return msg_referer_user_id[language]
async def msg_referer_user_id_func(message, language, referer_code, user_id):
    msg_referer_user_id = {
        'ru': f'Администратором @{message.from_user.username} добавлен партнер в реферальной системе: referer_code: {referer_code}, user_id партнера: {user_id}',
        'en': f"By the administrator @{message.from_user.username } added a partner in the referral system: referrer_code: {referer_code}, partner's user_id: {user_id}",
        'de': f'Administrator @{message.from_user.username } partner im Empfehlungssystem hinzugefügt: referrer_code: {referer_code}, user_id des Partners: {user_id}',
        'es': f'Administrador @ {message.from_user.username} socio agregado en el sistema de referencia: referrer_code: {referer_code}, user_id del socio: {user_id}',
        'pt': f'Administrador @{message.from_user.username} parceiro adicionado no sistema de referência: referrer_code: {referer_code}, user_id do parceiro: {user_id}',
        'iw': f'מנהל @{message.from_user.username} נוסף שותף במערכת ההפניה: referrer_code: {referer_code}, user_id של שותף: {user_id}',
        'zh': f'由管理员@{message.from_user.username }在推荐系统中添加了合作伙伴：referrer_code：{referer_code}，合作伙伴的user_id：{user_id}',
        'fr': f'Administrateur @{message.from_user.username} partenaire Ajouté dans le système de référence: referrer_code: {referer_code}, user_id du partenaire: {user_id}',
        'it': f'Amministratore @{message.from_user.username} aggiunto partner nel sistema di riferimento: referrer_code: {referer_code}, user_id partner: {user_id}'
    }
    return msg_referer_user_id[language]
async def msg_error(language):
    error_msg = {
        'ru': 'Произошла ошибка, попробуйте еще раз',
        'en': 'An error has occurred, please try again',
        'de': 'Es ist ein Fehler aufgetreten, versuchen Sie es erneut',
        'es': 'Se ha producido un error, inténtelo de nuevo',
        'pt': 'Ocorreu um erro, tente novamente',
        'iw': 'אירעה שגיאה, נסה שוב',
        'zh': '发生错误，请再试一次',
        'fr': "Une erreur s'est produite, essayez à nouveau",
        'it': 'Si è verificato un errore, riprova'
    }
    return error_msg[language]
async def del_referer_msg(language):
    msg = {
        'ru': 'Из базы данных удалён user_id:',
        'en': 'User id was deleted from the database:',
        'de': 'Die Benutzer-ID wurde aus der Datenbank entfernt:',
        'es': 'Id de usuario eliminado de la base de datos:',
        'pt': 'ID do Usuário removido do banco de dados:',
        'iw': 'מזהה משתמש הוסר ממסד הנתונים:',
        'zh': '用户id已从数据库中删除:',
        'fr': "ID utilisateur supprimé de la base de données:",
        'it': 'ID utente rimosso dal database:'
    }
    return msg[language]
async def admin_panel(message: types.Message, state: FSMContext):

    now_user_id = message.from_user.id
    language = await get_profile_language(now_user_id)
    user_ids = await get_partner_user_ids()
    flag = False
    print(user_ids)
    if user_ids != None:
        for user_id in user_ids:
            try:
                if int(user_id) == now_user_id:
                    flag = True
            except:
                pass
    if now_user_id == admin_id:
        flag = True
    if flag:
        await message.answer((await msg_menu(language)), reply_markup=(await create_admin_kb(language, message.from_user.id)))
    else:
        await message.answer((await msg_menu_no_cant(language)))

async def admin_panel_callback(call: types.CallbackQuery, state: FSMContext):
    if await state.get_data() != None:
        await state.finish()
    language = await get_profile_language(call.from_user.id)
    await call.message.edit_text(await msg_menu(language), reply_markup=(await create_admin_kb(language, call.from_user.id)))

async def view_statistic(call: types.CallbackQuery):
    user_id = call.from_user.id
    language = await get_profile_language(user_id)
    if call.data.split('_')[1] == 'common' and user_id == admin_id:
        count_all_users = await get_count_all_profiles()
        count_users_in_24hours = await get_count_profiles_in_24hours()
        count_clicks_on_1_btn = await get_count_clicks_on_1_btn()
        count_clicks_on_2_btn = await get_count_clicks_on_2_btn()
        await call.message.edit_text((await msg_view_statistic_common(count_all_users, count_users_in_24hours, count_clicks_on_1_btn, count_clicks_on_2_btn, language)), reply_markup=(await create_admin_back_menu_kb(language)))
    elif call.data.split('_')[1] == 'single':
        if user_id != admin_id:
            referer_code = await get_referer_code(user_id)
            count_start_users = await get_count_profiles_for_referer(referer_code)
            count_click_1_btn_users = await get_count_clicks_on_1_or_2_btn_for_referer('click_on_1_button', referer_code)
            count_click_2_btn_users = await get_count_clicks_on_1_or_2_btn_for_referer('click_on_2_button', referer_code)
            await call.message.edit_text((await msg_view_statistic_single(referer_code, count_start_users, count_click_1_btn_users, count_click_2_btn_users, language)), reply_markup=(await create_admin_back_menu_kb(language)))
        elif user_id == admin_id:
            all_referers = (await get_partner_referer_codes())
            print('Все рефералы', all_referers)

            msg = ''
            if all_referers != []:

                for referer_code in all_referers:
                    count_start_users = await get_count_profiles_for_referer(referer_code[0])
                    count_click_1_btn_users = await get_count_clicks_on_1_or_2_btn_for_referer('click_on_1_button', referer_code[0])
                    count_click_2_btn_users = await get_count_clicks_on_1_or_2_btn_for_referer('click_on_2_button', referer_code[0])
                    msg = msg + (await msg_view_statistic_single(referer_code[0], count_start_users, count_click_1_btn_users, count_click_2_btn_users, language))
                if len(msg) > 4095:
                    for x in range(0, len(msg), 4095):
                        await call.message.answer(msg[x:x + 4095], reply_markup=(await create_admin_back_menu_kb(language)))
                else:
                    await call.message.edit_text(msg, reply_markup=(await create_admin_back_menu_kb(language)))
            else:
                await call.message.edit_text((await msg_create_referal_to_view(language)), reply_markup=(await create_admin_back_menu_kb(language)))
    else:
        await call.answer(await msg_menu_no_cant(language))
    await bot.answer_callback_query(call.id)
async def add_referer(call: types.CallbackQuery):
    language = await get_profile_language(call.from_user.id)
    await call.message.edit_text((await msg_referer_func(call, language)), reply_markup=(await create_admin_back_menu_kb(language)))
    await Referers.referer_code.set()
    await bot.answer_callback_query(call.id)

async def add_referer_referer_code(message: types.Message, state: FSMContext):
    language = await get_profile_language(message.from_user.id)
    async with state.proxy() as data:
        data['referer_code'] = message.text
    await message.answer((await msg_referer_referer_code_func(message, language)), reply_markup=(await create_admin_back_menu_kb(language)))
    await Referers.user_id.set()

async def add_referer_user_id(message: types.Message, state: FSMContext):
    language = await get_profile_language(message.from_user.id)
    try:
        user_id = message.text
        async with state.proxy() as data:
            referer_code = data['referer_code']
        await input_partner_user_ids(referer_code, user_id)
        await message.answer((await msg_referer_user_id_func(message, language, referer_code, user_id)), reply_markup=(await create_admin_back_menu_kb(language)))
        await state.finish()
    except:
        await message.answer((await msg_error(language)))
async def delete_referer(call: types.CallbackQuery):
    language = await get_profile_language(call.from_user.id)
    try:
        partner_datas = await get_partner_datas()
        print(partner_datas)
        text1 = ''
        for list in partner_datas:
            text1 = f'{text1}{list[0]}: /del_{list[1]}\n'
        text0 = (await msg_menu(language)) + text1
        await call.message.answer(text0, reply_markup=(await create_admin_back_menu_kb(language)))
    except:
        await call.answer((await msg_error(language)))
    await bot.answer_callback_query(call.id)

async def delete_referer_phase2(message: types.Message):
    del_user_id = message.text.split('_')[1]
    language = await get_profile_language(message.from_user.id)
    await del_partner_data(del_user_id)
    text = await del_referer_msg(language)
    await message.answer(f'{text} {del_user_id}')


async def get_users_func(call: types.CallbackQuery):
    all_users = await get_all_users_db()
    print(all_users)
    try:
        with open("users.txt", "w") as file:
            for user_id in all_users:
                file.write(user_id[0] + '\n')
        f = open("users.txt", "rb")
        await bot.send_document(document=f, chat_id=call.from_user.id)
        remove("users.txt")
    except:
        await call.message.answer("Error")
    await bot.answer_callback_query(call.id)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(admin_panel, commands=['admin'], state="*")
    dp.register_callback_query_handler(admin_panel_callback, text=['admin'], state="*")
    dp.register_callback_query_handler(view_statistic, text_startswith=['statistic_'])
    dp.register_callback_query_handler(add_referer, text=['add_referer'])
    dp.register_message_handler(add_referer_referer_code, state=Referers.referer_code)
    dp.register_message_handler(add_referer_user_id, state=Referers.user_id)
    dp.register_callback_query_handler(delete_referer, text=['delete_referer'])
    dp.register_message_handler(delete_referer_phase2, text_startswith=['/del_'])
    dp.register_callback_query_handler(get_users_func, text=['get_users'])

