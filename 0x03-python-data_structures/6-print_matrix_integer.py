#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    mat_len = len(matrix)
    if mat_len == 0:
        print()
        return

    for row in range(mat_len):
        row_len = len(matrix[row])
        if row_len == 0:
            print()
            return

        for column in range(row_len):
            if column == row_len - 1:
                print("{:d}".format(int(matrix[row][column])))
            else:
                print("{:d}".format(int(matrix[row][column])), end=' ')
