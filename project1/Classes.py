# Классы. В основе ООП лежит понятие класса и объекта
# Инкапсуляция - сокрытие реализации от внешней стороны
# Наследование - возможность создания нового класса на базе существующего
# Полиморфизм - позволяет одинаково обращаться с объектами, имеющими однотипный интерфейс
# Класс - это шаблон для создания объектов
# Объект - это сущность, обладающуя определенным состоянием и поведением,
# имеющая свойства (атрибуты) и операции над ними (методы)

# Создание класса
class C:
    pass

# Создание объекта класса
Object_of_class = C

print(type(Object_of_class), "\n")

class Rectangle:
    default_colour = "green"
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

# АТРИБУТ default_colour - СТАТИЧЕСКИЙ. Т.е. к нему можно получить доступ, не
# создавая объекта класса Rectangle
print(Rectangle.default_colour)

# А вот АТРИБУТЫ width и heigth - ДИНАМИЧЕСКИЕ. К ним без создания объекта
# класса Rectangle уже не обратиться!!!
rect = Rectangle(10, 20)
print(rect.width, rect.heigth, "\n")

# При обращении к динамическим параметра через класс будет ошибка
# print(Rectangle.width) # Даже после точки автоматически не пытается дописать

# Можно присваивать новые значения статическим атрибутам
Rectangle.default_colour = "red"
print(Rectangle.default_colour)

# Для разных объектов данного класса default_colour теперь одинаковый
r1 = Rectangle(1, 2)
r2 = Rectangle(10, 30)
print(r1.default_colour)
print(r2.default_colour, "\n")

# При замене статического атрибута у одного объекта, у второго этот атрибут
# останется прежним и у самого класса тоже:
r1.default_colour = "blue"
print(r1.default_colour)
print(r2.default_colour)
print(Rectangle.default_colour, "\n")

# Метода класса
# Метод - это функция, находящаяся внутри класса и выполняющая определенную работу
# Метода: 1) статические; 2) классовые; 3) уровня класса (просто методы)

class MyClass:
    @staticmethod
    def ex_static_method():
        print("static method")

    @classmethod
    def ex_class_method(cls):
        print("class method")

    def ex_method(self):
        print("method")

# Статический и классовый методы можно вызывать без создания объекта класса
print(MyClass.ex_static_method())
print(MyClass.ex_class_method(), "\n")
# print(MyClass.ex_method()) # А вот тут уже выдает ошибку

# Создание объекта и обращение к методу
m = MyClass()
print(m.ex_method())
print(m.ex_static_method())
print(m.ex_class_method(), "\n")


# Конструктор класса и инициализация экземпляра класса
class RRectangle:
    def __new__(cls, *args, **kwargs):
        print("Hello from __new__")
        return super().__new__(cls)

    def __init__(self, width, heigth):
        print("Hello from __init__")
        self.width = width
        self.heigth = heigth

rect = RRectangle(10, 50)
print(rect.width)
print(rect.heigth, "\n")


# self   - это ссылка на текущий экземпляр. Позволяет получить доступ к артибутам
# и методам класса внутри него:
class Rctangle:
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def area(self):
        return self.width * self.heigth

RCT = Rctangle(10,40)
print(RCT.area(), "\n")

# Уровни доступа атрибута и метода
# Хороший тон: использовать для чтения и для изменения разные методы
# Также стоит выделять нижним подчериванием _ методы, которые извне не стоит трогать
# Причем, если выделить метода двумя подчеркиваниями __ то извне его не прочитать
class Rectangle2:
    def __init__(self, width, heigth):
        self._width = width
        self._heigth = heigth

    def get_width(self):
        return self._width

    def set_width(self, w):
        self._width = w

    def get_heigth(self):
        return self._heigth

    def set_heigth(self, h):
        self._heigth = h

    def area(self):
        return self._width * self._heigth

a = 10
b = 20
RCT2 = Rectangle2(a, b)
print(RCT2.get_heigth())
print(RCT2.get_width())
print(RCT2.area())
RCT2.set_heigth(24)
RCT2.set_width(100)
print(RCT2.get_heigth())
print(RCT2.get_width())
print(RCT2.area())
print(a,b, "\n")
# Здесь обращение к атрибутам объекта происходит через специальные методы
# Ничего не мешает обращаться к атрибутам напрямую
print(RCT2._heigth)
print(RCT2._width)

# Если задавать аналогичным образом, но использовать ДВА подчеркивания __
# то обратиться напрямую к атрибутам будет уже невозможно

class Rectangle3:
    def __init__(self, width, heigth):
        self.__width = width
        self.__heigth = heigth

    def get_wigth(self):
        return self.__width

    def get_heigth(self):
        return self.__heigth

    def set_width(self, w):
        self.__width = w

    def set_heigth(self, h):
        self.__heigth = h

    def area(self):
        return self.__width * self.__heigth

RCT3 = Rectangle3(11, 66)
print(RCT3.get_wigth(), RCT3.get_heigth())
# print(RCT3.__width, RCT3.__heigth) # Это не выводится, т.к. ошибка доступа


# Свойства - это метод класса. Позволяет осуществлять проверку входных значений
class Rectangle4:
    def __init__(self, width, heigth):
        self.__width = width
        self.__heigth = heigth

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError

    @property
    def heigth(self):
        return self.__heigth

    @heigth.setter
    def heigth(self, h):
        if h > 0:
            self.__heigth = h
        else:
            raise ValueError

    def area(self):
        return self.__width * self.__heigth

# Можно обращаться к атрибутам
rect = Rectangle4(10, 33)
print("\n", rect.heigth, rect.width)

# Можно даже изменять
rect.width = 100
rect.heigth = 77
print(rect.width, rect.heigth)

# Также было ограничение на положительность значения
# rect.width = -10






