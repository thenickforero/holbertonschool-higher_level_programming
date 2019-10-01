#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
        return True
    except (TypeError, ValueError) as error:
        import sys
        sys.stdout.write("Exception: {}\n".format(error))
        return False
