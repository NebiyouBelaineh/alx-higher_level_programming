#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number = abs(number)
        l_digit = number % 10
        print(l_digit, end="")
        return (l_digit)
    l_digit = number % 10
    print(l_digit, end="")
    return (l_digit)
