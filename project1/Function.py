# Функции. Есть лямбда-функции

# Создание функций
def fun1():
    pass


def fun2():
    return 1

print(fun2())


def summa(a,b):
    return a+b

print(summa(5,10), "\n")

# Функция нахождения числа Фибоначчи
def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        2+3
        return 1
    else:
        return fibb(n-1) + fibb(n-2)

print("Число фиббоначи от 10: {}".format(fibb(10)))


# Вычисление факториала
def factorial(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

print("Факториал от 5: {}".format(factorial(5)))

# Можно переменной присвоить функцию, чтобы сократить запись
import math
f = math.factorial
print(f(6), "\n")


# Lambda - функции. По сути, такая короткая функция для одной операции
print((lambda x: x**4)(3))

sqrt = (lambda x: x**0.5)
print(sqrt(16), "\n")

# map - это функция, которая сначала получает функцию, которую необходимо
# применить к каждому элементу списка, а потом сам список
lst = [1,2,3,4,5,6,7,8,9]
lst_new = list(map(lambda x: x**3, lst))
print(lst, lst_new)