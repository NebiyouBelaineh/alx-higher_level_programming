#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    result = 0
    if args == 1:
        print(result)
    else:
        for i in range(1, args):
            if args > 0:
                result += int(sys.argv[i])
        print(result)
