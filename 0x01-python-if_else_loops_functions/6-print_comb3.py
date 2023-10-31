#!/usr/bin/python3

for d2 in range(0, 9):
    for d1 in range(0, 10):
        if d1 > d2:
            if d2 == 8:
                print("{0:d}{1:d}".format(d2, d1))
                break
            print("{0:d}{1:d}".format(d2, d1), end=", ")
