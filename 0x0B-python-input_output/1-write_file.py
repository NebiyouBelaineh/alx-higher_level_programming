#!/usr/bin/python3
"""This module defines a funtion that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """This function writes a string to a text file with utf-8 encoding and
    returns the number of characters written"""
    written = 0
    with open(filename, "w", encoding="utf-8") as text_file:
        written += text_file.write(text)

    return written
