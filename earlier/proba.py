# from symbols import is_vowel
#
#
# def count_vowels(text):
#     result = 0
#     for char in text:
#         if is_vowel(char):
#             result += 1
#     return result

from symbols import is_vowel

def  count_vowels(words):
    words_1 = 0
    for words_2 in words:
        if is_vowel(words_2):
            words_1 += 1
    return words_1

print(is_vowel('a'))      # True
print(is_vowel('n'))      # False)

print(count_vowels('One'))  # 2
print(count_vowels('London is the capital of Great Britain'))  # 13


name = input('это конец!!!')


