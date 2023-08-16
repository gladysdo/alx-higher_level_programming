#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create an empty matrix to store the squared values
    squa_matrix = []
    # Iterate through the rows.
    for row in matrix:
        # Create a new row for the result matrix
        result_row = []
        # Iterate through current row
        for element in row:
            result_row.append(element ** 2)
        squa_matrix.append(result_row)
    return squa_matrix
