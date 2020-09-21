# Работа со списками

# Адреса переменных
a = 4
b = 5
print(id(a))
print(id(b))
a = b
print(id(a), "\n")

# Создание списка
# инициализация списка
a = []
print(type(a))
print(a)

# инициализация списка
b = list()
print(type(b))
print(b)

# инициализация списка
a = [1, 5, 4, 9]
print(type(a))
print(a)

# Создание копии списка
b = a[:]
print(b)

# Создание копии списка
c = list(a)
print(c)

# Создание копии списка
qwe = a.copy()
print(qwe)

# Создание ССЫЛКИ на другой список
d = a
print(d)

# Добавление элемента в существующй список в конец
a.append(3)
a.append("PRIV")

# Наглядное сравнение приравниваний списков
print(a, b, c, d)

# Удаление первого встреченного указанного элемента списка
a.remove(5)
print(a, b, c, d)

# Удаление элемента списка по индексу
del a[2] # индексация идет от нуля
print(a, b, c, d)

# Изменение элемента списка по индексу
a[0] = 77
print(a, b, c, d)

# Вывод диапазона из списка
print(a[1:4])

# Вывод длины списка
print(len(a))

# Добавление элементов в конец списка
a[len(a):] = [7789, 33]
print(a)

# Добавление списка к списку
a.extend(b)
print(a)

a[len(a):] = [55, 44, 11]
print(a)

# Вставка элемента (11111), начиная с определенного индекса (i)
a.insert(3, 11111)
print(a)

# Удаление и возвращение элемента по индексу. По сути, это вытаскивание элемента
print(a.pop(3))
# Производится операция с последним элементом
print(a.pop())
print(a)

# Удаление всех элементов списка
print(b,c)
del b[:]
c.clear()
print(b,c)

# Возвращение индекса элемента из списка
print(a.index("PRIV"))

# Возвращение количества вхождений элемента в список
a.insert(4, 77)
a.insert(7, 77)
a.insert(10, 77)
print(a)
print(a.count(77),"\n")

# del a[3]
a.remove("PRIV")

# Сортировка
print(a)
a.sort()
print(a)
a.sort(reverse = True)
print(a)



