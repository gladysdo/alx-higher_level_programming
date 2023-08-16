#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create an empty matrix to store square
    result_mat = []
    for row in matrix:
        # Create a new row
        result_row = []
        for element in row:
            result_row.append(element ** 2)
        result_mat.append(result_row)
    return result_mat
