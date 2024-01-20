from pyrogram import Client , filters
import sqlite3

api_id = 12345   #Пиши здесь api id
api_hash='WQJFQHQKL' #api hash
bot_token='Сюда вставляй токен бота'

botur = Client('bdshka',api_id=22651452,api_hash=api_hash, bot_token=bot_token)
bd1 = sqlite3.connect('users.db', check_same_thread=False)
cursor1 = bd1.cursor()
cursor1.execute('CREATE TABLE IF NOT EXISTS users(id_iser BIGINT PRIMARY KEY , status INT , url TEXT )')
cursor1.execute('CREATE TABLE IF NOT EXISTS admins(id_user BIGINT PRIMARY KEY)')


id_admins = [] # Список админов
chat_logi = -999999999 #Айди чата с логами
channel_id = -123456 #Айди канала
channel_url = 'https://t.me/123345' #Ссылка на канал 
author = 'https://t.me/da' #Ссылка на владельца