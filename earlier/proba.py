def my_substr(string, current_char):

    i = 0
    reversed_string = '' #  инициализируем строку, куда будем записывать результат
    current_char = string[i]    #   берем из строки символ по текущему индексу
    reversed_string = reversed_string + current_char #  записываем в строку-результат новое значение: текущая строка-результат + новый символ


    while i <= len(string): #   условие: повторяем тело цикла, пока текущий индекс не дошел — до последнего символа
        i = i + 1   #   обновляем счетчик

    return reversed_string  #   когда цикл завершился, возвращаем строку-результат




string = 'If I look back I am lost'

print(my_substr(string, 2))  # => 'I'
# print(my_substr(string, 7))  # => 'If I lo'


name = input('это конец')
