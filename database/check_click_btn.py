from create_bot import db, cur
# РАССЫЛКА СООБЩЕНИЕ В СЛУЧАЕ НЕНАЖАТИЯ НА КНОПКУ ПОСЛЕ 12 ЧАСОВ СТАРТА:
async def insert_in_button_clicks(user_id, first_name, click_time):
    cur.execute("INSERT OR IGNORE INTO button_clicks VALUES (?, ?, ?)", (user_id, first_name, click_time))
    db.commit()

async def get_data_from_button_clicks():
    return cur.execute('SELECT user_id, first_name, click_time FROM button_clicks').fetchall()
async def delete_data_from_button_clicks(user_id):
    cur.execute("DELETE FROM button_clicks WHERE user_id = ?", (user_id,))
    db.commit()

# ТАБЛИЦЫ, где хранятся нажатия на кнопки второго и третьего уровней
async def increase_in_clicks(db_lvl, user_id, click_time):
    # db_lvl: 'click_on_1_button' or 'click_on_2_button'
    referer = cur.execute("SELECT my_referer FROM profile WHERE user_id == '{key}'".format(key=user_id)).fetchone()[0]
    cur.execute("INSERT OR IGNORE INTO '{db_lvl}' VALUES (?, ?, ?)".format(db_lvl=db_lvl), (user_id, click_time, referer))
    db.commit()
