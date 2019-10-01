#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_elements_printed = 0
    for index in range(int(x)):
        try:
            print("{:d}".format(my_list[index]), end="")
            num_elements_printed += 1
        except (ValueError, TypeError):
            pass
    print()
    return num_elements_printed
