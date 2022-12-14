# name = input("Введите имя: ")
# print(name)
# name1 = "Dima"
# print(name == name1)
'''
name = input('Введите имя: ')
login = 'Dima'

if name == login:
    # выражение True
    print('Hello', name)
elif len(name) < 3:
    print('Такое имя недопустимо')
elif name == 'Yo':      # <- True
    print('Yo, bro')    # <- True
else:
    # выражение False
    print('Hello, user!')
'''

HELP = """
help - напечатать справку по программе.

add -  добавить задачу в список (название задачи запрашиваем у пользователя).

show - напечатать все добавленные задачи."""

# tasks = []

# run = True

# while run:
#     command = input("Введите команду: ")
#     if command == "help":
#         print(HELP)
#     elif command == "show":
#         print(tasks)
#     elif command == "add":
#         task = input("Введите название задачи: ")
#         tasks.append(task)
#         print("Задача добавлена")
#     else:
#         print("Неизвестная команда")
#         '''run = False или break'''
#         break

# print("До свидания!")

'''
x = 1
while x <=10:
    print(x)
    x = x + 1 #цикл для ограничения выполнения до 10

print(x) 
'''


i = 0
while i <= 10:
    print(i)
    i += 1
name = input('это конец')