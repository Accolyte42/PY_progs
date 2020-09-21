# Функция, определяющая високосность года
def is_year_leap(year):
    if year%4 == 0:
        return True
    else:
        return False
print(is_year_leap(2004))


# функция параметров квадрата
def square(a):
    temp = list()
    temp.append(4*a)
    temp.append(a**2)
    temp.append(a * (2 ** (1/2)))
    return tuple(temp)
print(square(3), type(square(3)))


# Банковской вклад
def bank(a,years):
    for i in range(years):
        a *= 1.1
    return a
print(bank(1000,5), '\n')


# Простые числа
def is_prime(a):
    t = a ** (1/2)
    t = int(t)
    flag = False
    for i in range(2,t+1):
        if a%i == 0:
            flag = True
            print(i, a)
    return flag
print(is_prime(18))

