#!/usr/bin/python3
"""This module defines a function that appends a string at the end of a text
file (UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """This function appends a string at the edn of a text file with encoding
    utf-8 and returns the number of characters added"""
    with open(filename, 'a', encoding='utf-8') as text_file:
        written = 0
        written += text_file.write(text)
    return written
