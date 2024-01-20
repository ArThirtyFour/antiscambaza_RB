import sqlite3
from osnova import id_admins , cursor1 , bd1 ,chat_logi



def add_bd(bot,message):
    user_id = int(message.from_user.id)
    cursor1.execute(f'SELECT id_user FROM admins WHERE id_user = {user_id}')
    if cursor1.fetchone() != None:
        try:
            text = message.text.split()
            id1 = int(text[1])
            status = int(text[2])
            url1 = text[3].replace('|',' , ')
            if status == 1:
                cursor1.execute('INSERT INTO users VALUES (?,?,?);', (id1, status, url1))
                bd1.commit()
                bot.send_message(message.chat.id, '✅ Добавлено!')
                bot.send_message(chat_logi,f'👮Администратор :\n🆔{user_id}\n - - - - - - - - - - - \nДействие: Добавление 🆔{id1} как скамера!🔴\n - - - - - - - - - - - \n📄 Пруфы :{url1}')
            elif status == 2:
                cursor1.execute('INSERT INTO users VALUES (?,?,?);', (id1, status, url1))
                bd1.commit()
                bot.send_message(message.chat.id, '✅ Добавлено!')
                bot.send_message(chat_logi,f'👮Администратор :\n🆔{user_id}\n - - - - - - - - - - - \n Действие: Добавление 🆔{id1} как гаранта!✅\n - - - - - - - - - - - \n📄 Пруфы :{url1}')
            else:
                bot.send_message(message.chat.id, f'❗️ Такой роли с статусом {status} не существует')
        except Exception as e:
            print(e)
            bot.send_message(message.chat.id,'🤡 - Бот выдал ошибку и не смог добавить. \n Это может быть связано с неправильным вводом ID/Уже внесен')
    else:
        bot.send_message(message.chat.id, '❗️ Вы не имеете права администратора.')


def deletebd(bot,message):
    user_id1 = int(message.from_user.id)
    cursor1.execute(f'SELECT * FROM admins WHERE id_user = {user_id1}')
    bd1.commit()
    if cursor1.fetchone() != None:
        try:
            text = message.text.split()
            id1 = int(text[1])
            cursor1.execute(f'DELETE FROM users WHERE id_iser = {id1};')
            bd1.commit()
            bot.send_message(message.chat.id, '✅ Удалено!')
            bot.send_message(chat_logi,f'👮Администратор :\n🆔{user_id1}\n - - - - - - - - - - - \nДействие: Удаление \n🆔{id1} из базы❗️')
        except Exception as e:
            print(e)
            bot.send_message(message.chat.id,'🤡 - Бот выдал ошибку и не смог удалить. \n Скорее всего связано с неправильным вводом ID/Нету в базе.')
    else:
        bot.send_message(message.chat.id, '❗️ Вы не имеете права администратора.')

def addadmin(bot,message):
    try:
        if message.from_user.id in id_admins:
            text = message.text.split()
            id_check = int(text[1])
            cursor1.execute(f'INSERT INTO admins VALUES ({id_check});')
            cursor1.execute(f'INSERT INTO users VALUES ({id_check},3,"da");')
            bd1.commit()
            bot.send_message(message.chat.id, '✅ Добавлено!')
        else:
            bot.send_message(message.chat.id, '❗️ Вы не имеете права администратора.')
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id,'🤡 - Бот выдал ошибку и не смог добавить. \n Скорее всего связано с неправильным вводом ID/Уже внесен.')
def deladmin(bot,message):
    try:
        if message.from_user.id in id_admins:
            id_delte=int(message.text.split()[1])
            cursor1.execute(f'DELETE FROM users WHERE id_iser = {id_delte};')
            cursor1.execute(f'DELETE FROM admins WHERE id_user = {id_delte};')
            bd1.commit()
            bot.send_message(message.chat.id, '✅ Удалено!')
        else:
            bot.send_message(message.chat.id, '❗️ Вы не имеете права администратора.')
    except:
        bot.send_message(message.chat.id,'🤡 - Бот выдал ошибку и не смог добавить. \n Скорее всего связано с неправильным вводом ID/Нету в базе.')