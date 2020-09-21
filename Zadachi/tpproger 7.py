# Нужно вывести первые n строк треугольника Паскаля. В этом
# треугольнике на вершине и по бокам стоят единицы, а каждое
# число внутри равно сумме двух расположенных над ним чисел.

# Решение мое
s = [1]
n = 8
print(s)
# n = input("введите n ")

for i in range(1,n):
    temp = s.copy()
    s.append(1)
    for j in range(1,i):
        s[j] = temp[j-1] + temp[j]
    print(s)


# Решение чужое
def pascal_triangle(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]

pascal_triangle(8)











