# Пробная программа

import math


# Просто вывод суммы
print(3+2, '\n')

# Сумма чисел
a = 4
b = 10
print(a+b, '\n')

# Сумма от одной переменной
a = 40
b = 13
c = a+b
print(c, '\n')

# Сложные операторы
a = 21
b = 9
a += b
print(a, '\n')

# Ещё сложные операторы
a = 44
b = 33
a -= b
print(a, '\n')

# Целая часть от деления
print(9//3)
a = 20
b = 7
print(a//b, '\n')

# возведение в степень
print(9**3)
a = 2
b = 5
print(a**b, '\n')

# Комплексные числа
z1 = -71 + 7j
print(z1)

# Части комплексного числа
z2 = complex(3,-2)
print(z2.real)
print(z2.imag)

# Комплексно-сопряженное
print(z2)
print(z2.conjugate(), '\n')

# Битовые операции
a = 1
b = 0
print(a&b)
print(a|b, '\n')

# Представление в двоичной системе
a = 31
print(bin(a), '\n')

# Библиотека math
x = 13.56
print(math.ceil(x))
print(math.floor(x))
print(math.factorial(5))
print(math.exp(3))
print(math.pow(16,2))
print(math.pow(16,1/2))

# Тригонометрия
pi = math.pi
print(math.cos(1.57))
print(math.sin(pi))
print(math.tan(3))
print(math.pi)
print(math.e)


