#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [[]]
    new_matrix = list(map(square, matrix))
    return (new_matrix)
def square(list=[]):
    return ([i**2 for i in list])
