#!/usr/bin/python3
"""Prints a square with the character #.

    Examples:
        >>> print_square(4)
        ####
        ####
        ####
        ####
        >>> print_square(1)
        #
        >>> print_square(0)
        <BLANKLINE>
    """


def print_square(size):
    """Print a square with # character.

    Args:
        size (int): is the length of the square

    Raises:
        TypeError: raised if size not an integer
        ValueError: raised if size is less than 0
    """
    if size == 0:
        print()
        return
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()


if __name__ == '__main__':
    import doctest
    doctest.testfile('./tests/4-print_square.txt')
