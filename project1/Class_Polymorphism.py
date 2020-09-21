# Полиморфизм - переопределение методов родительского класса
class Figure:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c

    def info(self):
        print("Figgggure")
        print("Color: " + self.__color)

class Rectangle(Figure):
    def __init__(self, width, heigth, color):
        super().__init__(color)
        self.__width = width
        self.__heigth = heigth

    @property
    def width(self, w):
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

    def info(self):
        print("Rectangle")
        print("Color: " + self.color)
        print("Width: " + str(self.__width))
        print("Heigth: " + str(self.__heigth))
        print("Area: " + str(self.area()))

    def area(self):
        return self.__width * self.__heigth

fig = Figure("orange")
fig.info()
rect = Rectangle(10, 20, "green")
rect.info()



