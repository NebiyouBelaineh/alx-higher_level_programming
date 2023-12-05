#!/usr/bin/python3
"""This module defines a function that reads a text file with utf-8 encoding"""


def read_file(filename=""):
    """This function reads a text file with utf-8 encoding and prints it to
    stdout"""
    with open(filename, 'r', encoding='utf-8') as text_file:
        for i in text_file:
            print(i, end="")
