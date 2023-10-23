#!/usr/bin/python3
def safe_print_integer(value):
    import sys
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as err:
        print("Exception:", err, file=sys.stderr)
        return False
    else:
        return True
