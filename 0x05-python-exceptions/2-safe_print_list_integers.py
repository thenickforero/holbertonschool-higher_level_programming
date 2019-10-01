#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_elements_printed = 0
    for index in range(int(x)):
        try:
            data = int(my_list[index])
        except (ValueError, TypeError):
            pass
        else:
            print("{}".format(data), end="")
            num_elements_printed += 1
    print()
    return num_elements_printed
