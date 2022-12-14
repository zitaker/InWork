'''
Задание 1
Модифицируйте нашего ЭхоБота таким образом, чтобы в ответ на сообщение, в котором присутствует ваше имя, он не повторял его, а отвечал: "Ба! Знакомые все лица!"

Подсказки
Вам не нужно писать новых функций, достаточно модифицировать ту, что мы написали на занятии.
Используйте конструкцию if word in string для того, чтобы проверить, входит ли слово word в строку string.

'''
import telebot

token = ''

bot = telebot.TeleBot(token)

my_name = 'Дима'


@bot.message_handler(content_types=["text"])
def echo(message):
    if my_name in message.text:
        text = 'Ба! Знакомые все лица'
    else:
        text = message.text
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)