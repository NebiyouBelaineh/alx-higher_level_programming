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
    """Divides 'matrix' by 'div' and returns a new list

    Args:
        matrix (list): a list of lists containing either an integer or a float
        div (int, float): scaler used to divide all elements of matrix list

    Raises:
        ZeroDivisionError: raised if div has the value of zero
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
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

    for n in matrix:
        if type(n) is not list:
            msg = "matrix must be a matrix (list of lists) of integers/floats"
            raise TypeError(msg)
        else:
            if size != len(n):
                msg = "Each row of the matrix must have the same size"
                raise TypeError(msg)
            msg = "matrix must be a matrix (list of lists) of integers/floats"
            for i in n:
                if type(i) not in [int, float]:
                    raise TypeError(msg)
                else:
                    sub_list.append(round((i / div), 2))
        new_list.append(sub_list)
        sub_list = []
    return new_list


if __name__ == '__main__':
    import doctest
    doctest.testfile('./tests/2-matrix_divided.txt')
