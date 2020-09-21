# Функция - это объект специального типа, поэтому её можно передавать другим
# функциям в качестве аргумента.
# Внутри функций можно создавать другие функции, вызывать их и возвращать как
# результат через return

# Функция как объект
# исходный список
a = [1,2,3,4,5]
# функция, возводящая переданное её число в квадрат
sq = lambda x: x**2
print(sq(7))

b = list(map(sq, a))
print(a, b, "\n")

# Функция - это специальный объект, у которого есть метод __call__()
class DemoCall():
    def __call__(self):
        return "Hello!!Kolyas"
HI = DemoCall()
print(HI())

# Можно вызывать и создавать функции внутри функций
def mul(a):
    def helper(b):
        return a/b
    return helper
# Вызывается такая функция так:
print(mul(4)(23), "\n")

three_mul = mul(3)
print(three_mul(5), "\n")
# Таким образом можно сделать вывод, что three_mul = mul(3) 3 - это аргумент a
# а print(three_mul(5)) - это аргумент b

# Декоратор - это функция, аргументом которой является другая функция.
# Декоратор необходим для добавления дополнительного функционала к данной функции
# без изменнеия содержимого последней
def first_test():
    print("Test finction 1")

def second_test():
    print("Test function 2")

# Хотим, чтобы до и после функций выводился ещё текст, но не изменяя тела функций
def simple_decore(fn):
    def wrapper():
        print("Run function")
        fn()
        print("Stop function")
    return wrapper()

# Обернем функции в оболочку:
first_test_wrapped = simple_decore(first_test)
second_test_wrapped = simple_decore(second_test)
print("")

first_test()
second_test()
print("\n")

first_test = first_test_wrapped
second_test = second_test_wrapped

first_test()
second_test()




