#!/usr/bin/python3

if __name__ == "__main__":
    from add_0 import add as addition
    a = 1
    b = 2
    print("{0:d} + {1:d} = {2:d}".format(a, b, addition(a, b)))
