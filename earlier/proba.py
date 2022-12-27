def normalize_url(url):
    normalize = url[:7]
    if normalize.replace('', 'https://'):
        print(normalize.replace('', 'https://', 1))
    elif normalize('http://'):
        print(normalize.replace('http://', 'https://', 1))
    else:
        print(normalize.replace('https://', 'https://', 1))
# s = 'hello'
# s1 = 'http://hello'
# s2 = 'https://hello'
# print(s.replace('', 'https://', 1) [:]) #работает
# print(s1.replace('http://', 'https://') [:])   #работает
# print(s2.replace('https://', 'https://') [:]) #работает

print(normalize_url('hello'))
print(normalize_url('http://hello'))
print(normalize_url('https://hello'))
name = input('это конец')
# если в первых 7 символах есть url то оставляем url, если url нет то добавляем его