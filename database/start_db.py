from create_bot import db, cur

def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, username TEXT, registration_time REAL, my_referer TEXT, language_interface TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS button_clicks(user_id TEXT PRIMARY KEY, first_name TEXT, click_time TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS click_on_1_button(user_id TEXT PRIMARY KEY, click_time REAL, referer TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS click_on_2_button(user_id TEXT PRIMARY KEY, click_time REAL, referer TEXT)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_language_interface ON profile (language_interface)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_my_referer ON profile (my_referer)")

    cur.execute("CREATE INDEX IF NOT EXISTS idx_click_time ON click_on_1_button (click_time)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_referer ON click_on_1_button (referer)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_click_time ON click_on_2_button (click_time)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_referer ON click_on_2_button (referer)")

    cur.execute("CREATE TABLE IF NOT EXISTS referers(referer_code TEXT PRIMARY KEY, user_id TEXT)")


    db.commit()