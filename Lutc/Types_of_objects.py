# Числа
print(123+222, type(123+222))
print(1.5*4, type(1.5*4))
print(2 ** 100, type(2 ** 100))
print(len(str(2 ** 1000)), "\n") # количество символов

# Можно импортировать math
import math
print(math.pi)
print(math.sqrt(23), "\n")

# Можно импортировать random
import random
print(random.random())
print(random.choice([1,2,3,4]))
a = [11,22,78,59,67,44,663,25]
print(random.choice(a), "\n")

# Операции над последовательностями
S = "SpamT"
print(len(S))
print(S[0])
print(S[1])
print(S[2], "\n")
print(S[-1]) # Индексация уже с конца
print(S[-2])
print(S[-3], "\n")

print(S)
print(S[1:3])
print(S[1:])
print(S[:4])
print(S[:-1]) # До последнего элемента
print(S[:], "\n") # все содержимое S

# стр.128
print(S)
print(S + "xyz") # конкатенация
print(S)
print(S * 8) # повторение

#
print(S)
# print(S[0] = "z") # нельзя изменять неизменяемые элементы
S = 'z' + S[1:] # но можно создавать новые объекты
print(S, "\n")

# Специфичные методы
print(S.find('pa')) # Находит позицию данной подстроки
print(S)
row = S.replace("pa", "XYZ") # Замена подстроки на другую подстроку в row
print(row)
print(S) # Но заменяет не исходную














