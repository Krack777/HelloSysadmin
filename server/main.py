import telebot
from telebot import types
from googleSheets import *

# config start

_pin = 1 # пинкод вашего бота (см п.1 readme)
token = ' ' # токен вашего тг бота (см п.2 readme)
spreadsheet_id = ' ' # id таблицы(см п.3 readme)
account_file = ' ' # расположение json файла с сервис учёткой(см п.4 readme)

# config end
table = Table(account_file=account_file, spreadsheet_id=spreadsheet_id)
user_status = {}
bot = telebot.TeleBot(token)
trusted_users = []


@bot.message_handler(commands=['start', 'help'])
def send_message(message):
    bot.reply_to(message, 'Здравствуйте, этот бот для удалённого доступа к эл. доске, все разработчики  уже давно в '
                          'аду, не беспокойтесь. '
                          ' Для меню напишите /menu или нажмите на кнопку')
    if not (message.from_user.id in trusted_users):
        bot.send_message(message.from_user.id, 'Вы не авторизованы! Введите пин код через /pin (пин-код)')


@bot.message_handler(commands=['pin'])
def pin_code(message):
    msg = message.text.split()
    try:
        if int(msg[1]) == _pin:
            trusted_users.append(int(message.from_user.id))
            bot.send_message(message.from_user.id, 'Пин-код верный! Вы авторизованы')
        else:
            bot.send_message(message.from_user.id, 'Увы, но пин-код не верный. Вы не авторизованы')
    except IndexError:
        bot.send_message(message.from_user.id, 'Вы не ввели пин-код после /pin')


@bot.message_handler(commands=['menu'])
def menu_zlo(message):
    if not (message.from_user.id in trusted_users):
        bot.send_message(message.from_user.id, 'Вы не авторизованы! Введите пин код через /pin (пин-код)')
        return
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Терминал', callback_data='terminal')
    btn2 = types.InlineKeyboardButton('Программа', callback_data='run')
    btn3 = types.InlineKeyboardButton('Картинка', callback_data='pic')
    btn4 = types.InlineKeyboardButton('Аудио', callback_data='audio')
    btn5 = types.InlineKeyboardButton('Запустить обновление', callback_data='update_True')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, 'Выберете, что запускать из списка', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def menu_zlo_answer(call):
    bot.answer_callback_query(callback_query_id=call.id,
                              text="Загрузка, ждите...")
    if call.data == 'terminal':
        bot.send_message(call.message.chat.id, 'Введите команду для выполнения в терминале')
        user_status[call.from_user.id] = 'ожидает_ввода_команды'

    elif call.data == 'run':
        bot.send_message(call.message.chat.id, 'Введите название программы для её запуска')
        user_status[call.from_user.id] = 'ожидает_ввода_программы'

    elif call.data == 'update_True':
        table.write('update=True')
        bot.send_message(call.message.chat.id, 'Обновление из репозитория GitHub запустится в '
                                               'ближайшее время')
    elif call.data == 'pic':
        bot.send_message(call.message.chat.id, 'Введите название картинки')
        user_status[call.from_user.id] = 'ожидает_ввода_картинки'

    elif call.data == 'audio':
        bot.send_message(call.message.chat.id, 'Введите название звука')
        user_status[call.from_user.id] = 'ожидает_ввода_звука'

    else:
        bot.send_message(call.message.chat.id, "Что-то пошло не так, попробуйте заново.")


@bot.message_handler(func=lambda message: user_status.get(message.from_user.id) == 'ожидает_ввода_программы')
def command_start_table(message):
    user_text = 'run=' + message.text
    table.write(user_text)
    user_status.pop(message.from_user.id, None)
    bot.send_message(message.chat.id, 'Сатана, программа будет открыта!')


@bot.message_handler(func=lambda message: user_status.get(message.from_user.id) == 'ожидает_ввода_картинки')
def command_start_table(message):
    user_text = 'image=' + message.text
    table.write(user_text)
    user_status.pop(message.from_user.id, None)
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
    bot.send_message(message.chat.id, 'Сатана, картинка будет открыта!')


@bot.message_handler(func=lambda message: user_status.get(message.from_user.id) == 'ожидает_ввода_звука')
def command_start_table(message):
    user_text = 'sound=' + message.text
    table.write(user_text)
    user_status.pop(message.from_user.id, None)
    bot.send_message(message.chat.id, f'Будет запущен звук: {message.text}')


@bot.message_handler(func=lambda message: user_status.get(message.from_user.id) == 'ожидает_ввода_команды')
def command_start_table(message):
    user_text = 'terminal=' + message.text
    table.write(user_text)
    user_status.pop(message.from_user.id, None)
    bot.send_message(message.chat.id, f'Будет запущена команда в терминале: {message.text}')


@bot.message_handler(commands=['update'])
def menu_update(message):
    if not (message.from_user.id in trusted_users):
        bot.send_message(message.from_user.id, 'Вы не авторизованы! Введите пин код через /pin (пин-код)')
        return

    markup = types.InlineKeyboardMarkup(row_width=2)
    update1 = types.InlineKeyboardButton('Обновить с перезапуском сейчас', callback_data='update_rebootNow')
    update2 = types.InlineKeyboardButton('Обновить без перезагрузки', callback_data='update_rebootLater')
    markup.add(update1, update2)
    bot.send_message(message.chat.id, 'Выберете тип обновления', reply_markup=markup)


@bot.message_handler(commands=['clear'])
def clear(message):
    if not (message.from_user.id in trusted_users):
        bot.send_message(message.from_user.id, 'Вы не авторизованы! Введите пин код через /pin (пин-код)')
        return
    i = 1
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    while True:
        try:
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - i)
            i += 1
        except Exception:
            break


bot.polling(none_stop=True)

