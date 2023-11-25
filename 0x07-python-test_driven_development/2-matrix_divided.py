#!/usr/bin/python3
"""
    Divides all elements of a matrix by div
    
    Examples:
        >>> matrix = [
            [1,2,3],
            [4,5,6]
            ]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
def matrix_divided(matrix, div):
    """
    Divides 'matrix' by 'div' and returns a new list
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    new_list = []
    sub_list = []
    if matrix:
        if matrix == []:
            return new_list 
        size = len(matrix[0])
    else:
        TypeError("")
    for n in matrix:
        if type(n) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        else:
            if size != len(n):
                raise TypeError("Each row of the matrix must have the same size")
            for i in n:
                if type(i) not in [int, float]:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                else:
                  sub_list.append(round((i / div), 2))
        new_list.append(sub_list)
        sub_list = []
    return new_list

if __name__ == '__main__':
    import doctest
    doctest.testfile('./tests/2-matrix_divided.txt')
