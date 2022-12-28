# def normalize_url(url):
#     normalize = url[:7]
#     # if normalize.replace('', 'https://'):
#     # if normalize.replace('', 'https://') == normalize.replace('', ''):
#     if normalize.replace('', 'https://') == normalize.replace('', '333'):
#         print(normalize.replace('', 'https://', 1))
#
#     elif normalize.replace('http://', 'https://'):
#         # print(normalize.replace('http://', 'https://'))
#         print(normalize.replace('http://', '111'))
#     # else:
#     #     print(normalize.replace('https://', 'https://'))
#     return "https://" + normalize
# # s = 'hello'
# # s1 = 'http://hello'
# # s2 = 'https://hello'
# # print(s.replace('', 'https://', 1) [:]) #работает
# # print(s1.replace('http://', 'https://') [:])   #работает
# # print(s2.replace('https://', 'https://') [:]) #работает
#
#
# print(normalize_url('hello'))
# print(normalize_url('http://hello1'))
# # print(normalize_url('https://hello2'))

# def normalize_url(url):
#     normalize = url[:-1]
#     if normalize == 'h':
#         # return '222'
#         return '444'
#     return '33'
#
# print(normalize_url('https://sdefw'))
# print(normalize_url('sdefw'))

# def get_type_of_sentence(sentence):
#
#   last_char = sentence[0]
#   if last_char == 'd':
#       return 'perviy'
#   elif last_char == '!':
#       return 'vtoroy'
#   return 'tretiy'


# print(get_type_of_sentence('dorn'))
# print(get_type_of_sentence('!http://Hodor?'))

# def normalize_url(url):
#     if 'https://' in url:
#         return url
#     elif 'http://' in url:
#         return 'https://' + url[7:]
#     else:
#         return 'https://' + url

def normalize_url(url):
    # if 'https://' in url:
    #     return url
    # elif url[0:3] != 'http':
    #     return 'https://' + url
    # elif 'http://' in url:
    #     return 'https://' + url[7:]
    url = url[0:]
    return url if 'https://' in url else 'https://' + url[7:]



print(normalize_url('hello'))
print(normalize_url('http://hello1'))
print(normalize_url('https://hello2'))
name = input('это конец')
# если в первых 7 символах есть url то оставляем url, если url нет то добавляем его