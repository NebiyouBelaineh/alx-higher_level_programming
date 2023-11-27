#!/usr/bin/python3
import numpy as np
"""This function uses NumPy package to calculate the product of two matrices
    Examples:
        >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
        [[ 7 10]
        [15 22]]
        >>> lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]])
        [[13 16]]
    """

    
def lazy_matrix_mul(m_a, m_b):
    """Returns the product of two matrices

    Args:
        m_a (list): The first matrix containing list of lists of integer or floats
        m_b (list): The second matrix containing list of lists of integer or floats

    Returns:
        array: return a NumPy array 
    """
    mat_a = np.array(m_a)
    mat_b = np.array(m_b)
    result = mat_a @ mat_b
    return result


if __name__ == '__main__':
    import doctest
    doctest.testfile('./tests/101-lazy_matrix_mul.txt')