def is_palindrome(word):
    return word == word[::-1]

a = "deeeeed"
print(is_palindrome(a))



def convert_seconds(time):
    days = time//(60*60*24)
    hours = (time - days*(60*60*24)) // (60 * 60)
    minutes = (time - days*(60*60*24) - hours*(60 * 60) ) // 60
    seconds = time - days*(60*60*24) - hours*(60 * 60) - minutes*60
    print('{}:{}:{}:{}'.format(days,hours,minutes,seconds))

convert_seconds(87000)
print(60*60*24)


# Принимается от пользователя последовательность чисел, разделенных
# запятой. Составить список и кортеж из них
# lst = map(int, input().split(','))
# a = list(lst)
# print(a)
# print(tuple(a))

# Вывести последний и первый элементы списка
lst = [1,2,3,4,5,6,7,8,9,10]
print(lst[0], lst[-1])


# При заданном целом числе n посчитать n + nn + nnn
n = str(4)
# print(type(n)) # type is str
nn = str(n) * 2
nnn = str(n) * 3
new_n = int(n) + int(nn) + int(nnn)
print(new_n, type(new_n))

# Чужое решение
def solve(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)

solve(4)
print()

# Написать программу, которая выводит четные числа из заданного списка
# и останавливается, если встречает число 237
lst1 = [4,5,873,342,4354,237, 22 ,3 , 78]

def vivod(lst):
    for i in range(0,len(lst),1):
        if lst[i] % 2 == 0:
            print(lst[i], end = " ")
        elif lst[i] == 237:
            break

vivod(lst1)
print()

# Программа, которая принимает два списка и выводит все элементы первого,
# которых нет во втором
lst1 = [1,2,3,4,5,6,7,8,9,10]
lst2 = [12,332,5,6,8,3,1,32432,7654,777,65, 7]

def func15(lst1, lst2):
    for i in lst1:
        flag = False
        for j in lst2:
            if i == j:
                flag = True
        if flag == False:
            print(i, end=" ")

func15(lst1, lst2)
print('\n')

# Вывести список файлов в указанной директории
# from os import listdir
# from os.path import isfile, join
# files = [f for f in listdir('/home') if isfile(join('/home', f))]
# print(files)


# Сложите цифры целого числа
n = 12332423432
n_str = str(n)
temp = 0
for i in n_str:
    temp += int(i)
print(n, temp, '\n')

# Посчитайте, сколько раз символ встречается в строке
str1 = "fdddefdssfdsgsagdsagdfdsa"
def count_of_char(str1, ch):
    temp = 0
    for i in str1:
        if i == ch:
            temp += 1
    return temp

print(count_of_char(str1, 'd'))

# Чужой вариант
string1 = 'Python Software Foundation'
print(string1.count('o'))


# Поменять значения местами
x = 5
y = 10
x, y = y, x


# С помощью анонимной функции извлеките из списка числа, делимые на 15.
nums = [45, 55, 60, 37, 100, 105, 220]
result = list(filter(lambda x: not x % 15, nums))
print(result)


# Нужно проверить, все ли числа в последовательности уникальны.
lst1 = [12, 1, 321, 43, 54, 654, 12, 142, 3223]


def uniq(lst1):
    flag = False
    for i in range(len(lst1)):
        for j in range(i+1,len(lst1)):
            if lst1[i] == lst1[j]:
                flag = True
    print(flag)
uniq(lst1)








