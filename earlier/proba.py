def string_or_not(or_not):
    return or_not and 'yes' or 'no'
    print(string_or_not())



string_or_not('Hexlet')  # yes
string_or_not(10)  # no
string_or_not('')  # yes
string_or_not(False)  # no


name = input('это конец')
