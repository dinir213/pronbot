from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import sqlite3 as sq
import asyncio
db = sq.connect('new.db')
cur = db.cursor()
loop = asyncio.get_event_loop()

# admin_id = 540058065
admin_id = 540058065

token = '6203880608:AAEBzfE8kzj0XQxhf90k6gPTVKvqwn3i8VE'
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
