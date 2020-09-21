# Генераторы и итераторы представляют собой инструменты, которые часто используются
# для поточной обработки.
num_list = [1, 62, 7, 48, 15]
for i in num_list:
    print(i)
print("\n")

itr = iter(num_list)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr), "\n")
# print(next(itr)) # Тут будет ошибка, т.к. больше нет элементов в списке

# Создание собственных итераторов. Если нужно в собственном классе что-то считать
class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

# Работа с элементами объекта в цикле for
s_iter2 = SimpleIterator(4)
for i in s_iter2:
    print(i)
print("\n")

# Генераторы
# Позволяют значительно упростить работу по конструирванию итераторов
# Генератор - это функция, при вызове её в next() возвращает следующий объект
# согласно алгоритму её работы
def siMMple_generator(val):
    while val > 0:
        val -= 1
        yield 2
# в данном примере при срабатывании функции yield цикл прекращается до следующего
# вызова функции next

gen_iter = siMMple_generator(5)
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))





















