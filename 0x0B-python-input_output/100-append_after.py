#!/usr/bin/python3
"""This module defines a function that inserts a line of text to a file
after each line containing a specific search string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file after each line containing a
    specific search string"""
    output = ""
    with open(filename, 'r', encoding='utf-8') as txt_file:
        for i in txt_file:
            output += i
            if search_string in i:
                output += new_string
    with open(filename, 'w', encoding='utf-8') as output_file:
        output_file.write(output)
