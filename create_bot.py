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

token = '6130281935:AAHQXn1NRrzfLDG0Z8aR5Ez1kH9poG5V6F8'
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
