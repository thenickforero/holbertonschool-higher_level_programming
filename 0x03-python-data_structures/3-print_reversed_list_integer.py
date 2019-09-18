#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        print()
    else:
        for item in reversed(my_list):
            print('{:d}'.format(item))
