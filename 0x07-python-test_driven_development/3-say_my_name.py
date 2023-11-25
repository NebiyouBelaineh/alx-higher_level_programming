#!/usr/bin/python3
"""Prints string:
"My name is <first name> <last name>", where <first name> and
    <last name> are passed as arguments

    Examples:
         >>> say_my_name("John", "Smith")
         My name is John Smith

         >>> say_my_name("Walter", "White")
         My name is Walter White

         >>> say_my_name("Bob")
         My name is Bob_ #_ is a space
    """


def say_my_name(first_name, last_name=""):
    """Prints first_name and last_name in the following format:
    --> "My name is <first name> <last name>"

    Args:
        first_name (str): first name string
        last_name (str, optional): last name string. Defaults to "".

    Raises:
        TypeError: Raised if first name not string
        TypeError: Raised if last name not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == '__main__':
    import doctest
    doctest.testfile('./tests/3-say_my_name.txt')
