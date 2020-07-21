import logging
import asyncio
import sqlite3
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config

connect = sqlite3.connect("user_data.db")       # создаем коннект к файлу БД
cursor = connect.cursor()                       # создаем объект курсор, позволяет нам управлять БД

cursor.execute("""CREATE TABLE IF NOT EXISTS user_data
                (id integer, full_name text, phone text, address text, order_data text)""")
connect.commit()                  # создать таблицу если она не существует, в скобках передаем названия и типы столбцовы

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)
loop = asyncio.get_event_loop()                         # Создаем: объект потока
bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")    # Обект бота
storage = MemoryStorage()                               # Объект памяти
dp = Dispatcher(bot=bot, storage=storage)               # Обект Dispatcher`a
