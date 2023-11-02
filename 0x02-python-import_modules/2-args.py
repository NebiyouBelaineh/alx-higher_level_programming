#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    if args == 1:
        print("0 arguments.")
    elif args > 1:
        print("{} argument{}:".format(args - 1, "s" if args > 2 else ""))
        for i in range(1, args):
            print("{}: {}".format(i, sys.argv[i]))
