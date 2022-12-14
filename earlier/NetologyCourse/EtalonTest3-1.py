'''
Задание 1
Реализуйте функцию count_letter, которая принимает список слов и некоторую букву и возвращает количество слов в списке, в которых эта буква встречается хотя бы один раз.

Например, для списка ['python', 'c++', 'c', 'scala', 'java'] и буквы c ваша функция должна вернуть число 3.

Подсказки
Используйте конструкцию for word in ... для итерации по списку.
Используйте переменную для хранения промежуточного результата подсчета.
Используйте конструкцию letter in word для проверки наличия буквы в слове.
'''

def count_letter(word_list, letter):
    result = 0
    for word in word_list:
        if letter in word:
            result += 1
    return result

print(count_letter(['python', 'c++', 'c', 'scala', 'java'], 'c'))

 
name = input('это конец')