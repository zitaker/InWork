from random import choice

import telebot

token = '5435515323:AAE4StbRid2jaAUQH9gtwVm_sPFshOd9nIo'

bot = telebot.TeleBot(token)


RANDOM_TASKS = ['Написать Гвидо письмо', 'Выучить Python', 'Записаться на курс в Нетологию', 'Посмотреть 4 сезон Рик и Морти']

todos = dict()


HELP = '''
Список доступных команд:
/ show  - напечать все задачи на заданную дату
/ add - добавить задачу
/ random - добавить на сегодня случайную задачу
/ help - Напечатать help
'''


def add_todo(date, task):
    date = date.lower()
    if todos.get(date) is not None:
        todos[date].append(task)
    else:
        todos[date] = [task]


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['random'])
def random(message):
    task = choice(RANDOM_TASKS)
    add_todo('сегодня', task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на сегодня')


@bot.message_handler(commands=['add'])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1]
    task = command[2]
    add_todo(date, task)
    if len(task) < 3:
        bot.send_message(message.chat.id, 'ошибка, вы ввели меньше 3х символов')
    else:
        text = 'Задача ' + task + ' добавлена на дату ' + date
        bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['show'])
def print_(message):
    date = message.text.split()[1].lower()
    if date in todos:
        tasks = ''
        for task in todos[date]:
            tasks += f'[ ] {task}\n'
    else:
        tasks = 'Такой даты нет'
    bot.send_message(message.chat.id, tasks)


bot.polling(none_stop=True)