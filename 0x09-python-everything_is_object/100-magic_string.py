#!/usr/bin/python3
def magic_string(s="BestSchool"):
    magic_string.counter = getattr(magic_string, 'counter', 0) + 1
    return ", ".join([s for i in range(magic_string.counter)])
