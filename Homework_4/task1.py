"""Напишите функцию для транспонирования матрицы"""

matrix = [[1,2,3], [4,5,6], [7,8,9]]

def print_mat(mat):
    for i in mat:
        print(i)
print_mat(matrix)

def transpon_matrix(matrix): #нужно положить значения 1 списка в 1 индексы остальных(поменять местами)
    matrix = list(zip(*matrix))
    return matrix
print("Единственный косячок - во втором случае (транс матрицы), все значения в кортежах")
print_mat(transpon_matrix(matrix))


