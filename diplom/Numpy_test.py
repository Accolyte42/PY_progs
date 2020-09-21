# Работа с массивами, математические операции над матрицами и векторами
# Линейная алгебра
import numpy as np

#
# Работа с встроенными матрицами
#

A = [[1, 4, 5],
     [-5, -8, 9]]
print(A)

A = [[1, 4, 5, 12],
     [-5, -8, 9, 0],
     [-6, 7, 11, 19]]
print("A = ", A)
print("A[1] = ", A[1])
print("A[1][2] = ", A[1][2])
print("A[0][-1] = ", A[0][-1])

column = [];
for row in A:
    column.append(row[2])

print("3rd column = ", column, '\n\nРабота с Numpy')

#
# Теперь сам NumPy
#

A = np.array([[1,2,3], [3,4,5]])
print(A,'\n')

A = np.array([[1.1,2,3], [3,4,5]])
print(A,'\n')

A = np.array([[1,2,3], [3,4,5]], dtype=complex)
print(A,'\n')

zeros_array = np.zeros( (2,3) )
print(zeros_array,'\n')

zeros_array = np.zeros( (2,3), dtype=np.int32 )
print(zeros_array,'\n')

A = np.arange(4)
print("A = ", A, "\n")

print('B =')
B = np.arange(12).reshape(3,4)
print(B, "\n")

A = np.array([[2,4], [5, -6]], dtype=np.int32)
B = np.array([[9,-3],[3,6]])
C = A+B
print(C, '\n')

# Умножение поэлементно
A = np.array([[3,6,7], [5,-3,0]])
B = np.array([[1,1], [2,1], [3,-3]])
C = B.dot(A)
print(C, "\n")

# Транспонирование матриц
A = np.array([[1,1], [2,1], [3,-3]])
print(A.transpose(), "\n")
print(A, '\n',A[2][1], "\n")

A = np.array([2,4,6,8,10])
print("A[0] = ", A[0])
print("A[2] = ", A[2])
print("A[-1] = ", A[-1], "\n")


# Поступ к элементам
A = np.array([[1, 4, 5, 12],
              [-5, 8, 9, 0],
              [-6, 7, 11, 19]])

print("A[0] = ", A[0])
print("A[2] = ", A[2])
print("A[-1] = ", A[-1])

print("A[0][0] = ", A[0][0])
print("A[1][2] = ", A[1][2])
print("A[1][-1] = ", A[1][-1])


# Доступ к столбцам
A = np.array([[1, 4, 5, 12],
              [-5, 8, 9, 0],
              [-6, 7, 11, 19]])

print("A[:,0] = ", A[:,0])
print("A[:,3] = ", A[:,3])
print("A[:,-1] = ", A[:,-1], '\n\n')


# Разделение матрицы
letters = np.array([1,3,5,7,9,11,5, 45])

print(letters[2:5])
print(letters[:5])
print(letters[5:])
print(letters[:]) # аналогично print(letters[:])
print(letters[::-1], '\n\n')

A = np.array([[1, 4, 5, 12, 14],
              [-5, 8, 9, 0, 17],
              [-6, 7, 11, 19, 21]])

print(A[:2, :4], "\n") # две строки, четыре столбца
print(A[:1,], "\n")  # первая строка, все столбцы
print(A[:,2], "\n") # все строки, второй столбец
print(A[:,2:5], "\n") # все строки, с третьего по пятый столбец
print(A[:1,2:], "\n") # все строки, со второй (она же единаствненая)
print(A[:,2:5], "\n") # все строки, с третьего по пятый столбец

