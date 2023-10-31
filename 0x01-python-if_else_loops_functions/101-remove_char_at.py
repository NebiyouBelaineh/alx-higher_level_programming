#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return (str)
    copy = list(str)
    copy[n] = ''
    str_cpy = ''
    for i in copy:
        str_cpy += i + ''
    return (str_cpy)
