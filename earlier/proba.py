def normalize_url(url):
    normalize = url[:7]
    # if normalize.replace('', 'https://'):
    # if normalize.replace('', 'https://') == normalize.replace('', ''):
    if normalize.replace('', 'https://') == normalize.replace('', '333'):
        print(normalize.replace('', 'https://', 1))

    elif normalize.replace('http://', 'https://'):
        # print(normalize.replace('http://', 'https://'))
        print(normalize.replace('http://', '111'))
    # else:
    #     print(normalize.replace('https://', 'https://'))
    return "https://" + normalize
# s = 'hello'
# s1 = 'http://hello'
# s2 = 'https://hello'
# print(s.replace('', 'https://', 1) [:]) #работает
# print(s1.replace('http://', 'https://') [:])   #работает
# print(s2.replace('https://', 'https://') [:]) #работает


print(normalize_url('hello'))
print(normalize_url('http://hello1'))
# print(normalize_url('https://hello2'))
name = input('это конец')
# если в первых 7 символах есть url то оставляем url, если url нет то добавляем его