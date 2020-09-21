# Наследование. Необходимо минимум два класса: родитель и потомок.
# Возможно и наследование от нескольких родителей

class Figure:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c

class Rectangle(Figure):
    def __init__(self, width, heigth, color):
        super().__init__(color)
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

rect = Rectangle(10, 20, "green")
print(rect.heigth, rect.width, rect.color)
rect.color = "red" # здесь происходит обращение к методу из родительского класса
print(rect.color)