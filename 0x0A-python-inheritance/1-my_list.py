#!/usr/bin/python3
"""This module defines a class Mylist that inherits from list"""


class MyList(list):
    """Class Mylist that inherits from list class"""

    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self, *args):
        """Prints the list in a sorted order"""
        print(sorted(self))


if __name__ == '__main__':
    import doctest
    doctest.testfile('./tests/1-my_list.txt')
