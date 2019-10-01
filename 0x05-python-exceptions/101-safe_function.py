#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        response = fct(*args)
        return response
    except Exception as error:
        import sys
        sys.stderr.write("Exception: {}\n".format(error))
        return None
