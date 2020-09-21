# Пример спискового включения
print("Введите число элемементо списка")
# n = int(input())
n = 7
a = [i for i in range(n)]
print(a, "\n")

# Возведение в квадрат всех элементов цикла
# В лоб через обращение к элементам списка
a = [1, 2, 3, 4, 5, 6]
b = []
for i in a:
    b.append(i ** 2)
print(a)
print(b, "\n")

# Использование map
a = [1, 2, 3, 4, 5, 6]
b = list(map(lambda x: x**2, a))
print('a = {}\nb = {}\n'.format(a,b))

# Само списковое включение (list comprehensions)
a = [1, 2, 3, 4, 5, 6]
b = [i**2 for i in a]
print('a = {}\nb = {}\n'.format(a, b))

# Выписывание ттолько четных чисел
# Поэлементно
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = []
for i in a:
    if i%2 == 0:
        b.append(i)
print('a = {}\nb = {}\n'.format(a,b))

# Использование filter
a = [1, 2, 3, 4, 5, 6,7,8]
b = list(filter(lambda x: x%2 ==0,a))
print('a = {}\nb = {}\n'.format(a,b))

# Использование спискового включения (list comprehensions)
a = [1, 2, 3, 4, 5, 6,7,8]
b = [i for i in a if i%2 == 0]
print('a = {}\nb = {}\n'.format(a,b))


