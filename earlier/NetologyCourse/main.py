# cat: кошка
#bat: летучая мышь
# ключ : значение

dictionary = {
    "cat": "кошка",
    "bat": "летучая мышь"
}

# print(dictionary)
# cat = dictionary["cat"]
# print(cat)

name = input("Введите имя: ")
print("Привет", name)

countries = {
    "Африка": ["Египет", "Конго", "ЮАР"],
    "Азия": ["Китай", "Таиланд", "Индонезия"]
}

africa = countries["Африка"]
print(africa)

africa_key = "Африка"
print(countries[africa_key])

countries["Европа"] = ["Австралия", "Испания", "Италия"]
print(countries)
print(countries["Европа"])
# countries[0] = "Hello"
# print(countries)
africa.append("Эфиопия")
print(africa)
print(countries)
print(len(countries["Африка"]))

name = input('это конец')

