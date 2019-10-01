#!/usr/bin/python3
def safe_print_integer(value):
    try:
        data = int(value)
        print("{:d}".format(data))
        return True
    except (ValueError, TypeError):
        return False
