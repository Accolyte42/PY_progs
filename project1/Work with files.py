# Для открытия файла используется open()
f = open("Numberss.txt", "r")
print("file.closed: " + str(f.closed))
print("file.mode: " + str(f.mode))
print("file.name: " + str(f.name), "\n")

# Чтение данных из файла осуществляется методами read() и readline()
# print(f.read(), "\n")

# Можно указывать требуемое количество читаемых символов
print(f.read(80), "\n")
f.close()

# Можно построчное считываение сделать через readline()
f = open("Numberss.txt", "r")
print(f.readline())
f.close()

# Построчное считывание можно организовать с помощью for
f = open("Numberss.txt", 'r')
for line in f:
    print(line)
f.close()

# Записывание в файл
f = open("New.txt", "a")
f.write("Test string in new file")
f.close()

# Дополнительные методы работы
f = open("Numberss.txt", "r")
print(f.read(5))
print(f.tell())
f.close()
print("\n")

# Выставление позиции в файле методом seek
f = open("Numberss.txt", "r")
print(f.tell()) # Тут текущая позиция в начале
f.seek(8) # Выставление необходимой позиции
print(f.read(1)) # Прочитать символ после 8-го
print(f.tell()) # Тут текущая позиция в начале
print(f.closed)
f.close()
print(f.closed)
print("\n")

# Ещё один вариант работы с файлами with. Не требуется закрывать файл
with open("Numberss.txt", "r") as f:
    for line in f:
        print(line, end="")
print(f.closed) # На выводе будет true, т.е. f закрыто





































