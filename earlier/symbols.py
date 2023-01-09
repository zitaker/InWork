# def is_vowel(text):
#     ya = 0
#     vowel = 'eyuioa'
#     if text.lower() in vowel:
#         ya += 1
#         return True
#     else:
#         return False
#     return text in vowel

def is_vowel(text):
    vowel = 0
    text_vowel = 'eyuioa'
    if text.lower() in text_vowel:
        vowel += 1
        return True
    else:
        return False

    return text in text_vowel

