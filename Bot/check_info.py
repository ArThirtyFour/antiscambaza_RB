import sqlite3
from datetime import datetime
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from osnova import id_admins

bd1 = sqlite3.connect('users.db', check_same_thread=False)

cursor1 = bd1.cursor()

def check(bot,message):
    try:
        ids = message.text.split()[1]
        global ad
        global name
        if ids[0] == '@':
            try:
                name = bot.get_users(user_ids=ids).first_name
                username = bot.get_users(user_ids=ids).username
            except:
                name = 'Не найдено'
                username= 'Не найдено'
            ad = bot.get_users(user_ids=ids).id
        else:
            try:
                name = bot.get_users(user_ids=ids).first_name
                username = bot.get_users(user_ids=ids).username
            except:
                name = 'Не найден'
                username= 'Не найден'
            ad = int(ids)
        cursor1.execute(f'SELECT * FROM users WHERE id_iser = {ad}')
        bd1.commit()
        a = cursor1.fetchone()
        btn1 = InlineKeyboardButton('Вечная ссылка', url=f'tg://user?id='+str(ad))
        markup2 = InlineKeyboardMarkup([[btn1]])
        try:
            if a[1] == 1:
                message.reply_text(f'| 💼  Я просмотрел по {ad} -  и что сказать... \n| ⛔️ Он находится в базе как скамер!\n| 📱 Имя пользователя: {name} \n| 🈵 Юзернейм - @{username} \n| 🕒 Дата проверки - {datetime.now().strftime("%Y.%m.%d %H:%M:%S")}\n| 📄 Доказательства: {a[2]}',reply_markup=markup2,quote=True)
            elif a[1] == 2:
                message.reply_text(f'| 💼  Я просмотрел по {ad} и что сказать... \n| ✅ Он находится в базе как гарант. Можете идти через него\n| 📱 Имя пользователя: {name }\n| 🈵 Юзернейм - @{username}\n| 🕒 Дата проверки - {datetime.now().strftime("%Y.%m.%d %H:%M:%S")}\n| 📄 Доказательства: {a[2]}',reply_markup=markup2,quote=True)
            elif a[1] == 3 and not ad  in id_admins:
                message.reply_text(f'| 💼  Я просмотрел по {ad} и что сказать... \n| 👮 Он находится в базе как администратор. Так что может принять если тебя заскамили \n| 📱 Имя пользователя: {name }\n| 🈵 Юзернейм - @{username} \n| 🕒 Дата проверки - {datetime.now().strftime("%Y.%m.%d %H:%M:%S")}',reply_markup=markup2,quote=True)
            elif a[1] == 3 and ad in id_admins:
                message.reply_text(f'| 💼  Я просмотрел по {ad} и что сказать... \n| 🔅 Он находится в базе как Владелец проекта  \n| 📱 Имя пользователя: {name } \n| 🈵 Юзернейм - @{username}\n| 🕒 Дата проверки - {datetime.now().strftime("%Y.%m.%d %H:%M:%S")}',reply_markup=markup2,quote=True)
        except:
            message.reply_text(f'| 💼  Я просмотрел по  {ad} и что сказать... \n| ❓️ Он НЕ находится в базе.\n| 📱 Имя пользователя: {name}\n| 🈵Юзернейм - @{username} \n| 🕒 Дата проверки - {datetime.now().strftime("%Y.%m.%d %H:%M:%S")}',reply_markup=markup2,quote=True)
    except Exception as e:
        print(e)
        message.reply_text('🤡 - Бот выдал ошибку и не смог проверить. \n Скорее всего связано с неправильным вводом.',quote=True)


def check_you(bot,message):
    user_id = int(message.from_user.id)
    try:
        name = bot.get_users(user_ids=user_id).first_name
        username = bot.get_users(user_ids=user_id).username
    except:
        name = 'Не найден'
        username = 'Не найден'
    cursor1.execute(f'SELECT * FROM users WHERE id_iser = {user_id}')
    bd1.commit()
    a = cursor1.fetchone()
    btn1 = InlineKeyboardButton('Вечная ссылка', url=f'tg://user?id=' + str(user_id))
    markup2 = InlineKeyboardMarkup([[btn1]])
    try:
        if a[1] == 1:
            message.reply_text(f'| 💼  Я просмотрел по {user_id} -  и что сказать... \n| ⛔️ Он находится в базе как скамер!\n| 📱 Имя пользователя: {name} \n| 🈵 Юзернейм - @{username} \n | 🕒 Дата проверки - {datetime.now().strftime("%Y.%m.%d %H:%M:%S")}\n| 📄 Доказательства: {a[2]}',reply_markup=markup2, quote=True)
        elif a[1] == 2:
            message.reply_text(f'| 💼  Я просмотрел по {user_id} и что сказать... \n| ✅ Он находится в базе как гарант. Можете идти через него\n| 📱 Имя пользователя: {name}\n| 🈵 Юзернейм - @{username}\n| 🕒 Дата проверки - {datetime.now().strftime("%Y.%m.%d %H:%M:%S")}\n| 📄 Доказательства: {a[2]}',reply_markup=markup2, quote=True)
        elif a[1] == 3 and user_id not in id_admins:
            message.reply_text(f'| 💼  Я просмотрел по {user_id} и что сказать... \n| 👮 Он находится в базе как администратор. Так что может принять если тебя заскамили \n| 📱 Имя пользователя: {name}\n| 🈵 Юзернейм - @{username} \n| 🕒 Дата проверки - {datetime.now().strftime("%Y.%m.%d %H:%M:%S")}',reply_markup=markup2, quote=True)
        elif a[1] == 3 and user_id in id_admins:
            message.reply_text(f'| 💼  Я просмотрел по {user_id} и что сказать... \n| 🔅 Он находится в базе как Владелец проекта  \n| 📱 Имя пользователя: {name} \n| 🈵 Юзернейм - @{username}\n| 🕒 Дата проверки - {datetime.now().strftime("%Y.%m.%d %H:%M:%S")}',reply_markup=markup2, quote=True)
    except:
        message.reply_text(f'| 💼  Я просмотрел по  {user_id} и что сказать... \n| ❓️ Он НЕ находится в базе.\n| 📱 Имя пользователя: {name}\n| 🈵Юзернейм - @{username} \n| 🕒 Дата проверки - {datetime.now().strftime("%Y.%m.%d %H:%M:%S")}',reply_markup=markup2, quote=True)

def about(bot, message):
    cursor1.execute('SELECT id_iser , url FROM users WHERE status = 2')
    bd1.commit()
    spisok1 = '✅Оффицальные гаранты базы\n - - - - - - - - - - - \n Формат: (🔠Имя,🆔 ID, 📕Пруфы)\n- - - - - - - - - - -\n'
    b = cursor1.fetchall()
    for garant in b:
        try:
            name= bot.get_users(user_ids=garant[0]).first_name
        except:
            name = 'Не удалось получить'
        spisok1 = spisok1  +f' 🔠 - {name}\n 🆔 - {garant[0]} \n 📕 - {garant[1]}\n- - - - - - - - - - -\n'
    cursor1.execute('SELECT id_iser , url FROM users WHERE status = 3')
    bd1.commit()
    spis2 = '👮 Оффицальные Админы базы \n - - - - - - - - - - - \n Формат: (🔠Имя,🆔 ID )\n- - - - - - - - - - -\n'
    c = cursor1.fetchall()
    for admin_id1 in c:
        try:
            name1 = bot.get_users(user_ids=admin_id1[0]).first_name
        except:
            name1 = 'Не удалось получить'
        spis2 = spis2 + f' 🔠 - {name1}\n 🆔 - {admin_id1[0]} \n- - - - - - - - - - -\n'
    full_spisok = spisok1 + '\n\n\n' + spis2
    message.reply_text(f'Интерсная информация про проект \n 💾 | Написан в Октябре 2023 года  \n 🆘 | Версия: 1.0 (Релиз) \n 💍 | Формально владельца 2 - 1 кодер , а второй и есть владелец  \n\n\n {full_spisok}',quote=True)