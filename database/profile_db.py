import time

from create_bot import cur, db

async def create_profile(message, my_referer, language_interface, registration_time):
    user_id = message.from_user.id
    username = message.from_user.username
    user = cur.execute("SELECT * FROM profile WHERE user_id=?", (user_id,)).fetchall()
    if not user:
        cur.execute("INSERT INTO profile VALUES (?, ?, ?, ?, ?)", (user_id, username, registration_time, my_referer, language_interface))
        db.commit()
    else:
        referer_id = user[0][3]
        print(f'Ваш профиль уже зарегистрирован по ссылке от реферала с user_id: {referer_id}')
async def get_profile(user_id):
    return cur.execute("SELECT * FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()
async def get_profile_language(user_id):
    return cur.execute("SELECT language_interface FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()[0]

async def check_args(referer, user_id: int):
    all_languages_interface = ['ru', 'en', 'de', 'es', 'pt', 'iw', 'zh', 'fr', 'it']
    try:
        referer = referer.split("_")
    except:
        return ['0', 'en']
    if referer == '':
        return ['0', 'en']
    elif len(referer) == 2:
        for language in all_languages_interface:
            if referer[1] == language:
                return referer
        return ['0', 'en']
    #     устанавливаем язык по умолчанию EN

    else:
        return ['0', 'en']

# Статистика
async def get_count_all_profiles():
    return cur.execute("SELECT COUNT(*) FROM profile").fetchone()[0]
async def get_count_profiles_in_24hours():
    now_time = int(time.time()) - 86400
    select_query = "SELECT COUNT(*) FROM profile WHERE registration_time >= ?"
    return cur.execute(select_query, (now_time,)).fetchone()[0]

async def get_count_clicks_on_1_btn():
    return cur.execute("SELECT COUNT(*) FROM click_on_1_button").fetchone()[0]
async def get_count_clicks_on_2_btn():
    return cur.execute("SELECT COUNT(*) FROM click_on_2_button").fetchone()[0]

async def get_count_profiles_for_referer(referer_code):
    select_query = "SELECT COUNT(*) FROM profile WHERE my_referer = ?"
    return cur.execute(select_query, (referer_code,)).fetchone()[0]
async def get_count_clicks_on_1_or_2_btn_for_referer(btn, referer_code):
    print(btn, referer_code)
    select_query = f"SELECT COUNT(*) FROM {btn} WHERE referer = ?"
    return cur.execute(select_query, (referer_code,)).fetchone()[0]
async def get_referer_code(user_id):
    return cur.execute("SELECT referer FROM referers WHERE user_id == '{key}'".format(key=user_id)).fetchone()[0]
