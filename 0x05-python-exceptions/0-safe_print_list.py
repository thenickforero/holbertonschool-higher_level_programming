#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    failed = False
    for i in range(int(x)):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            failed = True
            break
    print()
    return i + 1 if not failed else i
