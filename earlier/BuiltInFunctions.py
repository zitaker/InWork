'''Встроенные функции, выполняющие преобразование типов ниже
bool(x) - преобразование к типу bool, использующая стандартную процедуру проверки истинности. Если х является ложным или опущен, возвращает значение False, в противном случае она возвращает True.

bytearray([источник [, кодировка [ошибки]]]) - преобразование к bytearray. Bytearray - изменяемая последовательность целых чисел в диапазоне 0≤X<256. Вызванная без аргументов, возвращает пустой массив байт.

bytes([источник [, кодировка [ошибки]]]) - возвращает объект типа bytes, который является неизменяемой последовательностью целых чисел в диапазоне 0≤X<256. Аргументы конструктора интерпретируются как для bytearray().

complex([real[, imag]]) - преобразование к комплексному числу.

dict([object]) - преобразование к словарю.

float([X]) - преобразование к числу с плавающей точкой. Если аргумент не указан, возвращается 0.0.

frozenset([последовательность]) - возвращает неизменяемое множество.

int([object], [основание системы счисления]) - преобразование к целому числу.

list([object]) - создает список.

memoryview([object]) - создает объект memoryview.

object() - возвращает безликий объект, являющийся базовым для всех объектов.

range([start=0], stop, [step=1]) - арифметическая прогрессия от start до stop с шагом step.

set([object]) - создает множество.

slice([start=0], stop, [step=1]) - объект среза от start до stop с шагом step.

str([object], [кодировка], [ошибки]) - строковое представление объекта. Использует метод __str__.

tuple(obj) - преобразование к кортежу.
Встроенные функции, выполняющие преобразование типов выше'''

'''Другие встроенные функции ниже
abs(x) - Возвращает абсолютную величину (модуль числа).

all(последовательность) - Возвращает True, если все элементы истинные (или, если последовательность пуста).

any(последовательность) - Возвращает True, если хотя бы один элемент - истина. Для пустой последовательности возвращает False.

ascii(object) - Как repr(), возвращает строку, содержащую представление объекта, но заменяет не-ASCII символы на экранированные последовательности.

bin(x) - Преобразование целого числа в двоичную строку.

callable(x) - Возвращает True для объекта, поддерживающего вызов (как функции).

chr(x) - Возвращает односимвольную строку, код символа которой равен x.

classmethod(x) - Представляет указанную функцию методом класса.

compile(source, filename, mode, flags=0, dont_inherit=False) - Компиляция в программный код, который впоследствии может выполниться функцией eval или exec. Строка не должна содержать символов возврата каретки или нулевые байты.

delattr(object, name) - Удаляет атрибут с именем 'name'.

dir([object]) - Список имен объекта, а если объект не указан, список имен в текущей локальной области видимости.

divmod(a, b) - Возвращает частное и остаток от деления a на b.

enumerate(iterable, start=0) - Возвращает итератор, при каждом проходе предоставляющем кортеж из номера и соответствующего члена последовательности.

eval(expression, globals=None, locals=None) - Выполняет строку программного кода.

exec(object[, globals[, locals]]) - Выполняет программный код на Python.

filter(function, iterable) - Возвращает итератор из тех элементов, для которых function возвращает истину.

format(value[,format_spec]) - Форматирование (обычно форматирование строки).

getattr(object, name ,[default]) - извлекает атрибут объекта или default.

globals() - Словарь глобальных имен.

hasattr(object, name) - Имеет ли объект атрибут с именем 'name'.

hash(x) - Возвращает хеш указанного объекта.

help([object]) - Вызов встроенной справочной системы.

hex(х) - Преобразование целого числа в шестнадцатеричную строку.

id(object) - Возвращает "адрес" объекта. Это целое число, которое гарантированно будет уникальным и постоянным для данного объекта в течение срока его существования.

input([prompt]) - Возвращает введенную пользователем строку. Prompt - подсказка пользователю.

isinstance(object, ClassInfo) - Истина, если объект является экземпляром ClassInfo или его подклассом. Если объект не является объектом данного типа, функция всегда возвращает ложь.

issubclass(класс, ClassInfo) - Истина, если класс является подклассом ClassInfo. Класс считается подклассом себя.

iter(x) - Возвращает объект итератора.

len(x) - Возвращает число элементов в указанном объекте.

locals() - Словарь локальных имен.

map(function, iterator) - Итератор, получившийся после применения к каждому элементу последовательности функции function.

max(iter, [args ...] * [, key]) - Максимальный элемент последовательности.

min(iter, [args ...] * [, key]) - Минимальный элемент последовательности.

next(x) - Возвращает следующий элемент итератора.

oct(х) - Преобразование целого числа в восьмеричную строку.

open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True) - Открывает файл и возвращает соответствующий поток.

ord(с) - Код символа.

pow(x, y[, r]) - ( x ** y ) % r.

reversed(object) - Итератор из развернутого объекта.

repr(obj) - Представление объекта.

print([object, ...], *, sep=" ", end='\n', file=sys.stdout) - Печать.

property(fget=None, fset=None, fdel=None, doc=None)

round(X [, N]) - Округление до N знаков после запятой.

setattr(объект, имя, значение) - Устанавливает атрибут объекта.

sorted(iterable[, key][, reverse]) - Отсортированный список.

staticmethod(function) - Статический метод для функции.

sum(iter, start=0) - Сумма членов последовательности.

super([тип [, объект или тип]]) - Доступ к родительскому классу.

type(object) - Возвращает тип объекта.

type(name, bases, dict) - Возвращает новый экземпляр класса name.

vars([object]) - Словарь из атрибутов объекта. По умолчанию - словарь локальных имен.

zip(*iters) - Итератор, возвращающий кортежи, состоящие из соответствующих элементов аргументов-последовательностей.
Другие встроенные функции выше'''

'''
print(p) round(p) - 'Округление'
float.as_integer_ratio() - пара целых чисел, чьё отношение равно этому числу.

float.is_integer() - является ли значение целым числом.

float.hex() - переводит float в hex (шестнадцатеричную систему счисления).

classmethod float.fromhex(s) - float из шестнадцатеричной строки

import math - 'предоставляет более сложные математические функции'
import random - 'реализует генератор случайных чисел и функции'

'''
'''
Методы словарей ниже
dict.clear() - очищает словарь.

dict.copy() - возвращает копию словаря.

classmethod dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).

dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).

dict.items() - возвращает пары (ключ, значение).

dict.keys() - возвращает ключи в словаре.

dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).

dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.

dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default (по умолчанию None).

dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).

dict.values() - возвращает значения в словаре.
Методы словарей выше

__new__(cls[, ...]) — управляет созданием экземпляра. В качестве обязательного аргумента принимает класс (не путать с экземпляром). Должен возвращать экземпляр класса для его последующей его передачи методу __init__.

__init__(self[, ...]) - 'перегружает конструктор класса' как уже было сказано выше, конструктор.

__del__(self) - вызывается при удалении объекта сборщиком мусора.

__repr__(self) - вызывается встроенной функцией repr; возвращает "сырые" данные, использующиеся для внутреннего представления в python.

__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.

__bytes__(self) - вызывается функцией bytes при преобразовании к байтам.

__format__(self, format_spec) - используется функцией format (а также методом format у строк).

__lt__(self, other) - x < y вызывает x.__lt__(y).

__le__(self, other) - x ≤ y вызывает x.__le__(y).

__eq__(self, other) - x == y вызывает x.__eq__(y).

__ne__(self, other) - x != y вызывает x.__ne__(y)

__gt__(self, other) - x > y вызывает x.__gt__(y).

__ge__(self, other) - x ≥ y вызывает x.__ge__(y).

__hash__(self) - получение хэш-суммы объекта, например, для добавления в словарь.

__bool__(self) - вызывается при проверке истинности. Если этот метод не определён, вызывается метод __len__ (объекты, имеющие ненулевую длину, считаются истинными).

__getattr__(self, name) - вызывается, когда атрибут экземпляра класса не найден в обычных местах (например, у экземпляра нет метода с таким названием).

__setattr__(self, name, value) - назначение атрибута.

__delattr__(self, name) - удаление атрибута (del obj.name).

__call__(self[, args...]) - вызов экземпляра класса как функции.

__len__(self) - длина объекта.

__getitem__(self, key) - доступ по индексу (или ключу).

__setitem__(self, key, value) - назначение элемента по индексу.

__delitem__(self, key) - удаление элемента по индексу.

__iter__(self) - возвращает итератор для контейнера.

__reversed__(self) - итератор из элементов, следующих в обратном порядке.

__contains__(self, item) - проверка на принадлежность элемента контейнеру (item in self).
'''

'''
Перегрузка арифметических операторов ниже
__add__(self, other) - сложение. x + y вызывает x.__add__(y).

__sub__(self, other) - вычитание (x - y).

__mul__(self, other) - умножение (x * y).

__truediv__(self, other) - деление (x / y).

__floordiv__(self, other) - целочисленное деление (x // y).

__mod__(self, other) - остаток от деления (x % y).

__divmod__(self, other) - частное и остаток (divmod(x, y)).

__pow__(self, other[, modulo]) - возведение в степень (x ** y, pow(x, y[, modulo])).

__lshift__(self, other) - битовый сдвиг влево (x << y).

__rshift__(self, other) - битовый сдвиг вправо (x >> y).

__and__(self, other) - битовое И (x & y).

__xor__(self, other) - битовое ИСКЛЮЧАЮЩЕЕ ИЛИ (x ^ y).

__or__(self, other) - битовое ИЛИ (x | y).

Пойдём дальше.

__radd__(self, other),

__rsub__(self, other),

__rmul__(self, other),

__rtruediv__(self, other),

__rfloordiv__(self, other),

__rmod__(self, other),

__rdivmod__(self, other),

__rpow__(self, other),

__rlshift__(self, other),

__rrshift__(self, other),

__rand__(self, other),

__rxor__(self, other),

__ror__(self, other) - делают то же самое, что и арифметические операторы, перечисленные выше, но для аргументов, находящихся справа, и только в случае, если для левого операнда не определён соответствующий метод.

Например, операция x + y будет сначала пытаться вызвать x.__add__(y), и только в том случае, если это не получилось, будет пытаться вызвать y.__radd__(x). Аналогично для остальных методов.

Идём дальше.

__iadd__(self, other) - +=.

__isub__(self, other) - -=.

__imul__(self, other) - *=.

__itruediv__(self, other) - /=.

__ifloordiv__(self, other) - //=.

__imod__(self, other) - %=.

__ipow__(self, other[, modulo]) - **=.

__ilshift__(self, other) - <<=.

__irshift__(self, other) - >>=.

__iand__(self, other) - &=.

__ixor__(self, other) - ^=.

__ior__(self, other) - |=.

__neg__(self) - унарный -.

__pos__(self) - унарный +.

__abs__(self) - модуль (abs()).

__invert__(self) - инверсия (~).

__complex__(self) - приведение к complex.

__int__(self) - приведение к int.

__float__(self) - приведение к float.

__round__(self[, n]) - округление.

__enter__(self), __exit__(self, exc_type, exc_value, traceback) - реализация менеджеров контекста.
Перегрузка арифметических операторов выше
'''

'''
split(maxsplit=2) - 'игнорировать пробелы (расщеплять)'
message_handler - 'обработчик сообщений'
a.lower() - 'нижний регистр'
reload() - 'перезагрузить модуль' из стандартной библиотеки importlib. Перезагрузка не влияет на объекты, ссылающиеся на импортированный модуль, и позволяет реализовать динамическую перезагрузку компонентов программы.
raise - 'выполнить в любом случае (поднимать, возбудить исключение)'
'''