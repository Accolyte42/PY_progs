import keyword
import builtins

print(keyword.kwlist)

help(abs)  # по сути, ctrl+q
print(dir())

print(dir(builtins), "\n")

# Регистр имеет значение!
x = 10
X = 3232
print(x, X, "\n")

# Типы данных
print(type(True), type(False))
print(int(True), int(False))
print(type(5.4), type(8.5e-3))
print(type(2+2j))
print(type("Stroka"))
print(type( [1, 2, 3] )) # Список
print(type( (1, 2, 3) )) # Кортежи
print(type( range(1,10) )) # Диапазон
print(type( {"x": 5, "y": 20} )) # Словарь
print(type( {"a", "b", "c"} ) ) # Множество
print(type(frozenset( ["a", "b", "c"] ) ) ) # Множество неизменяемое
print()

#
str1 = "avto"
str2 = "transport"
str3 = str1 + str2
print(str3, "\n")

arr = [1, 2]
i = iter(arr)
print(i.__next__()) # метод обхода элементов
print(next(i), "\n") # функция обхода элементов

# для словарей
d = {"x": 1, "y": 2}
i = iter(d)
print(i.__next__()) # Возвращает ключ
print(d[i.__next__()], "\n") # Получение значения по ключу

# Вывод можно организовывать циклом for
for i in [1, 2, 3, 7]:
    print(i)
print()

# Перебор можно и по строке так:
for i in "Stroka":
    print(i + " -", end = " ")
print("\n")

# Перебор элементов словаря
d = {"x": 20, "y": 3}
for key in d:
    print( d[key], end = " ")
print("\n")

# Хитрое присваивание
x = y = [1, 2]
print(x, y)

y[1] = 100
print(x, y, "\n") # Как видно, обе переменные ссылаются на один и тот же объект

x = [1, 2]
y = [1, 2]
y[1] = 100
print(x, y)
print(x is y , "\n")

xx = yy = [1, 2] # Ссылаются на один и тот же объект
print(xx is yy)
x = [1, 32] # Разные объекты
y = [1, 32] # Разные объекты
print(x is y, "\n")

# Иногда в целях эффективности кода ссылки на один и тот же объект
x = 2; y = 2; z = 2
print(x is y, y is z, "\n")

# Хитрое присвоение
x, y, z = 1, 2, 3
print(x, z)
print(x, y, z, "\n")

a, b = 1, 2; a, b = b, a
print(a,b, "\n")

# Можно присваивать и последовательности
x, y, z = "123"
print(x,y,z)
x,y,z = [1,2,3]
print(x,y,z)
x,y,z = (1,2,3)
print(x,y,z)
[x,y,z] = (1,2,3)
print(x,y,z)

# Ошибка несоответствтия количества переменных и вводных элементов
# x, y, z = (1, 2, 3, 4)

# При несоответствии количества можно использовать оператор (*)
x, y, *z = (1,2,3,4,5)
print(x,y,z)
x, *y, z = (1,2,3,4,5)
print(x,y,z)
*x, y, z = (1,2,3,4,5)
print(x,y,z)
x, y, *z = (1,2,3)
print(x,y,z)
x, y, *z = (1,2)
print(x,y,z)
# Ошибкой будет:
# *x, y, *z = (1,2,3,4,5)

# Преобразование типов данных
a = int("123")
print(a + 5, "\n")

# Получение данных от пользователя. Т.к. нет преобразования типов, то получим строку
# x = input("x = ")
# y = input("y = ")
# print(x + y, "\n") # выводится строка

# x = int(input("x = "))
# y = int(input("y = "))
# print(x + y, "\n") # выводится строка

# Удаление переменных можно делать
x = 10
print(x)
del x
# print(x) # Тут будет ошибка

x, y = 10, 32
del x, y








