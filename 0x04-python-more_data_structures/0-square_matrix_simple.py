#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for rows in range(len(matrix)):
        new_mat.append(list(map(lambda x : x**2, matrix[rows])))

    return new_mat
