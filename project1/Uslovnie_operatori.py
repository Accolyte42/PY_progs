# Условные операторы

a = 60
if a < 10:
    print(a)
    print("//")
elif (10 < a < 50):
    print("else")
    print("||")
else:
    print("max")
    print("--")

print("Условий конец")


# /////////////////     Циклы       ////////////////

# Работа while
b = 1
while b < 10:
    b += 1
    print(b, " ")

print("\n")

# Работа с break. Досрочно прерывает цикл
c = 0
while c <= 100:
    c += 1
    if c == 7:
        break
    print(c, " ")

print("\n")

# Работа с continue. Запускает цикл заново
d = -1
while d < 10:
    d += 1
    if d >= 4:
        continue
    print(d)

print("\n")

# Работа for
for i in range(5):
    print(i)

print("\n")

# Работа со списком
lst = [1, 3, 5, 7, 9, 78]
for i in lst:
    print(i*2)

print("\n")

# Проход по всем буквам в строке:
word_str = "Hello, world!"
for i in word_str:
    print(i)

print("\n")



