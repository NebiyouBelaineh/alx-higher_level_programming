#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print()
    else:
        for i in matrix:
            for j in i:
                print("{:d}".format(j), end="")
                print("{}".format(" " if j != i[len(i) - 1] else ""), end="")
            print()
