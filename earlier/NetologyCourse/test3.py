# def multiply(a, b):
#     print("a = ", a)
#     print("b = ", b)
#     result = a * b
#     return result

# # c = multiply(3, 5)
# # print(c)
# # c = multiply(4, 6)
# # print(c)
# # c = multiply(7, 8)
# # print(c)

# def print_hello():
#     print("hello")
#     print("world")

# print_hello()
# print_hello()

# def my_input(prompt):
#     print(prompt)
#     inp = ...
#     return inp

import random

today = list()
tomorrow = list()
other = list()

HELP = """
help - напечатать справку по программе.
add -  добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
random - добавлять случайную задачу на дату."""

# RANDOM_TASK = "записаться"
RANDOM_TASKS = "Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"

tasks = {
    
}
run = True

def add_todo(date, task):
    if date in tasks:
            # дата есть в словаре
            # добавляем в список задачу
        tasks[date].append(task)
    else: 
            # даты в словаре нет
            # создаем запись с ключом date
        tasks[date] = []
        tasks[date] = [task] 
    print("Задача добавлена", task, "добавлена на дату: ", date)

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка задач: ")
        if date in tasks:
            for task in tasks[date]:
                print('* ', task)
            else:
                print("Такой даты нет")
    elif command == "add":
        date = input("Введите дату для добавления задачи: ")
        task = input("Введите название задачи: ")
        add_todo(date, task)

        
    elif command == "random":
        task = random.choice(RANDOM_TASKS)
        add_todo("сегодня", task)
    # elif command == "random_date":
    #     add_todo(RANDOM_DATE, RANDOM_TASK) добавлять другую функцию
        # if "сегодня" in tasks:
        #     tasks["сегодня"].append(RANDOM_TASK)
        # else:
        #     tasks["сегодня"] = []
        #     tasks["сегодня"].append(RANDOM_TASK)
    else:
        print("Неизвестная команда")
        '''run = False или break'''
        break


name = input('это конец')