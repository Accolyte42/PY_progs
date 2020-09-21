# Tuple - это кортеж. Это неизменяемся структура данных. Похожа на список
# В отличие от списка, он НЕИЗМЕНЯЕМЫЙ
# Нужен когда мы не собираемся менять исходный массив.
# Экономичный относительно списка
a = (1, 2, 3, 4, 5, 6)
print("a = {}".format(a))

lst = [10, 20, 30]
tpl = (10, 20, 30)

print(lst.__sizeof__())
print(tpl.__sizeof__(), "\n")

# Создание кортежа
a = ()
b = tuple()
print("type a = {}\ntype b = {}\ntype lst = {}\n".format(type(a),type(b),type(lst)))

# Преобразование кортежа в список и обратно
lst1 = [1, 2, 7, 8, 10]
tpl1 = tuple(lst1)
print(lst1, tpl1)
print("lst1 type is {}\ntpl1 type is {}\n".format(type(lst1),type(tpl1)))

tpl2 = (43, 65, 654, 123)
lst2 = list(tpl2)
print(tpl2, lst2)
print("tpl2 type is {}\nlst2 type is {}\n".format(type(tpl2),type(lst2)))
