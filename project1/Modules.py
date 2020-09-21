# В модулях хранятся часто используемые функции. классы, константы и т.д.
# Можно импортировать сразу несколько модулей через запятую
# import math, datetime
# print(math.factorial(7))
# print(math.cos(math.pi/4))
# print(datetime.date(2000, 8, 5))

# Можно подулю сразу дать псевдоним
# import math as m
# print(m.sin(m.pi/6), "\n")

# Можно импортировать некоторые конкретные функции из модуля
# from math import cos, pi, sin
# print(cos(pi/5))
# print(sin(pi/5))

# можно импортировать объект сразу с псевдонимом
# from math import cos as cs, pi as p
# print(cs(p/5))

# можно импортировать все объекты
# from math import *
# print(cos(pi/5))
# print(sin(pi/5))
# print(factorial(6))

# Пакеты. Пакет - это каталог модулей. Т.е. в нем много модулей и импортировать можно часть
import cv2
image = cv2.imread("photo.jpg")
(h,w,d) = image.shape
print("width={}, heigth={}, depth={}".format(w,h,d))

cv2.imshow("Kolyas portrait", image)
cv2.waitKey(0)





