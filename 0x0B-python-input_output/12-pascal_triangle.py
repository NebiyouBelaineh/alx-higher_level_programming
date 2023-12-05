#!/usr/bin/python3
"""This module defines a function that returns a list of integers representing
the Pascal's triangle of 'n'"""


def pascal_triangle(n):
    """Returns a list of list that represents the Pascal's triangle for a
    given number 'n'

    Args:
        n (int): integer parameter

    Returns:
        pascal_list (list): list of lists of integers representing the Pascal's
        triangle
    """
    if n <= 0:
        return []

    final_list = [[1]]

    while len(final_list) != n:

        sub_list = final_list[-1]
        sub = [1]

        for i in range(len(sub_list) - 1):
            sub.append(sub_list[i + 1] + sub_list[i])

        sub.append(1)
        final_list.append(sub)

    return final_list
