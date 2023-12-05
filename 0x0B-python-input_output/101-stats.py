#!/usr/bin/python3
"""This module defines a function that reads from STDIN line by line
    and computes metrics
    """


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_num = 0

    try:
        for line in sys.stdin:
            if line_num == 10:
                print("File size: {}".format(size))
                for key in sorted(status_codes):
                    print("{}: {}".format(key, status_codes[key]))
                line_num = 1
            else:
                line_num += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print("File size: {}".format(size))
        for key in sorted(status_codes):
            print("{}: {}".format(key, status_codes[key]))

    except KeyboardInterrupt:
        print("File size: {}".format(size))
        for key in sorted(status_codes):
            print("{}: {}".format(key, status_codes[key]))
        raise
