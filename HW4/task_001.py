# Напишите функцию для транспонирования матрицы transposed_matrix, 
# принимает в аргументы matrix, и возвращает транспонированную матрицу.

# def transpose(matrix):
#     # определяем количество строк и столбцов в матрице
#     rows = len(matrix)
#     cols = len(matrix[0])

#     # создаем новую матрицу с размерами, поменянными местами
#     transposed = [[0 for row in range(rows)] for col in range(cols)]

#     # заполняем новую матрицу значениями из старой матрицы
#     for row in range(rows):
#         for col in range(cols):
#             transposed[col][row] = matrix[row][col]

#     return transposed

# matrix = [[1, 2, 3],
#          [4, 5, 6], 
#          [7, 8, 9]]
# transposed_matrix = transpose(matrix)
# print(transposed_matrix)

def transpose(matrix):
    # Получим количество строк и столбцов в исходной матрице
    rows, cols = len(matrix), len(matrix[0])

    # Создадим новую матрицу для транспонирования
    transposed_matrix = [[0] * rows for _ in range(cols)]

    # Проходим по исходной матрице и копируем элементы в транспонированную матрицу
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

matrix = [[1, 2, 3],
         [4, 5, 6], 
         [7, 8, 9]]
transposed_matrix = transpose(matrix)
print(transposed_matrix)