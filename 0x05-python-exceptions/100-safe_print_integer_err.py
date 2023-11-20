#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as ve:
        print("Exception: {}".format(ve), file=sys.stderr)
        return False
    except TypeError as te:
        print("Exception: {}".format(te), file=sys.stderr)
        return False
    except NameError as ne:
        print("Exception: {}".format(ne), file=sys.stderr)
        return False
    else:
        return True
