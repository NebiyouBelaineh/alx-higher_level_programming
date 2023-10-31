#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            x = True
        else:
            x = False
        print("{:c}".format((ord(str[i]) - 32) if x else ord(str[i])), end="")
    print()
