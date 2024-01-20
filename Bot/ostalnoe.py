from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from osnova import channel_id ,channel_url , author
def started(bot,message):
    global user_id
    user_id = int(message.from_user.id)
    try:
        bot.get_chat_member(chat_id=channel_id, user_id=user_id)
        btn1 = InlineKeyboardButton('Гитхаб Автора', url='https://github.com/ArThirtyFour')
        btn2 = InlineKeyboardButton('Создатель №1(Кодер)', url='https://t.me/AR_34_2')
        btn3 = InlineKeyboardButton('Создатель №2(Владелец)', url=author)
        markup1 = InlineKeyboardMarkup([[btn1],[btn2,btn3]])
        bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name}! Мы предсталяем революционный проект, помогающий проверить людей на скам.\n🆘 | Как пользоваться ботом - /help\n🆔 | Ваш ID:{user_id}',reply_markup=markup1)
    except:
        btn = InlineKeyboardButton('Наш канал', url=channel_url)
        markup = InlineKeyboardMarkup([[btn]])
        bot.send_message(message.chat.id, 'Для пользования ботом , надо подписаться на канал', reply_markup=markup)


def help1(bot,message):
    bot.send_message(message.chat.id,'ПОЛНЫЙ СПИСОК КОМАНД :\n - - - - - - - - - - - \n /start - запуск бота \n /check (id/@Username) - проверет пользователя \n /help - выдаст список команд \n /status - Выведет инфу про бота\n /me - проверка себя\n- - - - - - - - - - - \n АДМИН КОМАНДЫ НЕ ПОКАЗЫВАЕТ!!!')