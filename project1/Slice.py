# Слайсы - это какие-то разрезы. Помогает быстро выбирать элементы
a = [i for i in range(10)]

print(a)
print(a[:])
print(a[0:5])
print(a[2:7])
print(a[::2])
print(a[1:8:2], "\n")

s = slice(1,9,3)

print(a[s])


