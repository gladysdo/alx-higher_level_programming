#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Module to check if matrix is a list of lists of integers or floats"""
    if not all(isinstance(row, list) and all(isinstance(element, (int, float))
        for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    """ Check if each row of the matrix has the same size"""
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    """ Check if div is a number (integer or float)"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    """ Check if div is not equal to 0"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    """ Divide all elements of the matrix by div, rounded to 2 decimal places"""
    result_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        result_matrix.append(new_row)
    
    return result_matrix
