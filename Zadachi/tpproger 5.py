# Найти три ключа с самыми выскоими занчениями в словаре
my_dict = {'a1': 700, 'b1': 5874, 'c1': 560,'d1': 400, 'e1': 5874, 'f1': 20, 'g1': 2444}

# мое решение
d = my_dict.copy()
print(d)
# print(d.values())
# print(d.keys())
# print(len(d))
# print(type(temp))

# варианты перебора словаря
for i in d.__iter__():
    print(i, end = " ")
print()

# эквивалентный вариант
for i in d:
    print(i, end = " ")
print()

vr = 0
l1 = []
l1.append
for i in d:
    l1.append(d[i])
    vr += 1
    # print(d[i], end = " ")
    # print(l1)

# По сути обратный словарь
# s = []
# for i in d.keys():
#     s.append((d[i], i))
# b = dict(s)
# print(b)
# print(b.pop(max(l1)))

result = sorted(d, key=d.get, reverse=True)
print(result[:3])

