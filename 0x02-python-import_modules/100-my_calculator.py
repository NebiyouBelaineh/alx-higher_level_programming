#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as cal
    import sys
    args = len(sys.argv)
    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    opt = sys.argv[2]
    if opt == '+':
        print("{0:d} + {1:d} = {2:d}".format(a, b, cal.add(a, b)))
    elif opt == '-':
        print("{0:d} - {1:d} = {2:d}".format(a, b, cal.sub(a, b)))
    elif opt == '*':
        print("{0:d} * {1:d} = {2:d}".format(a, b, cal.mul(a, b)))
    elif opt == '/':
        print("{0:d} / {1:d} = {2:d}".format(a, b, cal.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
