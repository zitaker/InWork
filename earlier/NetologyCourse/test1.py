'''
Задание 1
Напишите программу, которая последовательно запрашивает у пользователя Дату и Описание задачи, а затем выводит их через пробел.

Пример ввода-вывода программы:

Введите дату: Сегодня
Введите задачу: Сделать все дела
Сегодня Сделать все дела
'''
# Задание 1 ниже
print('Задание 1') # Задание 1
print(input('Введите дату:'))
print(input('Введите задачу:'))
str1 = 'Введите дату: '
str2 = 'Введите задачу:'
print(str1 + str2)
# Задание 1 выше
'''
Задание 2
Модифицируйте программу из задания 1 таким образом, чтобы запрос даты и задачи выполнялся трижды и после этого результаты выводились на экран построчно в формате: на одной строчке дата и задача через пробел.

Пример ввода-вывода программы:

Введите дату: Сегодня
Введите задачу: Выучить Python
Введите дату: Завтра
Введите задачу: Разработать TODO-приложение
Введите дату: Послезавтра
Введите задачу: Разработать Telegram-бота
Сегодня Выучить Python
Завтра Разработать TODO-приложение
Послезавтра Разработать Telegram-бота
'''
# Задание 2 ниже
print('Задание 2') # Задание 2
str3 = input('Введите дату: ')
str4 = input('Введите задачу: ')
str5 = input('Введите дату: ')
str6 = input('Введите задачу: ')
str7 = input('Введите дату: ')
str8 = input('Введите задачу: ')
print(str3, str4)
print(str5, str6)
print(str7, str8)
# Задание 2 выше

'''
Задание 3
Модифицируйте программу из задания 2 таким образом, чтобы данные не выводились на экран, а сохранялись в словарь. Ключами в этом словаре должны быть даты, а значениями - соответствующие им задачи.

Пример ввода программы:

Введите дату: Сегодня
Введите задачу: Выучить Python
Введите дату: Завтра
Введите задачу: Разработать TODO-приложение
Введите дату: Послезавтра
Введите задачу: Разработать Telegram-бота
Это задание не предполагает вывод информации на экран.

Подсказки
Для запроса данных у пользователя используйте функцию input.
Для вывода данных на экран используйте функцию print.
Сохраняйте нужные вам данные в переменные.
'''
# Задание 3 ниже
print('Задание 3') # Задание 3
# dictionary = {
#     '11.11.2022' : ['день рождения', 'неделя началась'],
#     '12.11.2022' : ['день второй', 'идем в магазин'], 
#     '13.11.2022' : ['заключительный день', 'вы остаетесь не дай бох или уходите слава богу']}

# days1 = dictionary['11.11.2022']
# days2 = dictionary['12.11.2022']
# days3 = dictionary['13.11.2022']


# days1.append(input('день рождения: '))
# days2.append(input('день второй: '))
# days3.append(input('заключительный день: '))

# print(days1)
# print(days2)
# print(days3)

# или
print('Задание 3') # Задание 3
dictionary = {}
days1 = input('Введите дату: ')
days2 = input('Введите задачу: ')
dictionary[days1] = days2

print(days1, days2)
print(dictionary)

# Задание 3 выше


input('это конец')