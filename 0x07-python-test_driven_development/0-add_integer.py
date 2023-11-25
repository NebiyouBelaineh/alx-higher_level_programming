#!/usr/bin/python3
"""Adds two numbers and returns their sum

    Examples:
        >>> add_integer(1, 2)
        3"""


def add_integer(a, b=98):
    """Returns the sum of two integers 'a' and 'b'

    Args:
        a (int, float): integer or float paramenter
        b (int, optional): integer or float parameter. Defaults to 98.

    Raises:
        TypeError: raised if a or b are not integer or float
        OverflowError: raised if float('inf') is passed to args a or b
        ValueError: raised if float('nan') passed to args a or b

    Returns:
        int : The sum of args a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if a is float('inf') or b is float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if a is float('nan') or b is float('nan'):
        raise ValueError("cannot convert float NaN to integer")
    return int(a) + int(b)


if __name__ == '__main__':
    import doctest
    doctest.testfile('./tests/0-add_integer.txt')
