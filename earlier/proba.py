def trim_and_repeat(text, offset = 0, repetitions = 1):
    result = (text[offset:] * repetitions)
    return result

print(trim_and_repeat('python'))


# def trim_and_repeat(text, offset = 0, repetitions = 1):
#     result = (text[offset:] * repetitions)
#     return result
# trim_and_repeat(text='BlackSilverUfa')
# print(trim_and_repeat)


# def truncate(text, length):
#     result = f"{text[0:length]}..."
#     return result
# print(truncate('qwerty qwerty123', 3))
name = input('это конец')