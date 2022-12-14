"""
print("привет")

print(2 + 5)
print(3 * 5)
print(18 / 77)
print(2 - 3 * 4)
print(5 * (2 - 5))
print(2 ** 4)
print(411 % 3)
"""
# strings = ["Hello", "world"]
# numbers = [1, 2, 3, 4, 5]
# data = ["hello", 1]

# print(strings)
# print(numbers)
# print(data)

# summa = numbers + data
# print(summa)

# numbers.append(22)
# print(numbers)

# first = strings[0]
# second = strings[1]
# print(first)
# print(second)

# strings_length = len(strings)
# print(strings_length)

# s = sum(numbers)
# print(s)

# print(data * 5)

# 15:44 09.11.2022 липецк -> москва 02:23 москва ВК восточный
# белорусский вокзал 06:20 10.11.2022 москва -> минск 13:10 10.11.2022 поезд
#                         23:05 10.11.2022 минск -> кутаиси 04:25 11.11.2022 самолет

# 05:25 18.11.2022 кутаиси -> минск 08:50 18.11.2022 самолет
#     21:44 18.11.2022 минск -> москва 06:54 19.11.2022 поезд белорусский вокзал
#         14:20 19.11.2022 москва казанская -> 20:42 19.11.2022 липецк

array = [1, 2, 3, 4, 5, 6, 7] # список из целых чисел int
print(type(array)) # класс list
ar = [2, 4.6, 'str', [1, 2, 3]] # список, состоящий из целого числа,
# из числа с плавающей точкой, из строки и из списка

print(array[0], array[1]) # печатаем 2 первых элемента в списке: 1 и 2
array[0] = 0 # в нулевой элемент списка кладем цифру 0

array.append(8)

array2 = [9, 10]
new_array = array + array2

new_array = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]

len(new_array)

sum(new_array)

new_array.append(1)
print(new_array)
new_array.sort()
print(new_array)

dictionary = {'dog' : 'собака', 'table' : 'стол', 'computer': 'компьютер'}

print(dictionary['dog']) # печатаем строку 'собака'
dictionary['dog'] = 'пес' # изменяем значение 'собака' на 'пес'
dictionary['laptop'] = 'ноутбук' # добавляем новый элемент с ключом 
# 'laptop' и значением 'ноутбук' в словарь


name = input('это конец')
