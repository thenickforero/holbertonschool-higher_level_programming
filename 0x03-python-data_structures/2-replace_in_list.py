#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if int(idx) < 0 or int(idx) + 1 > len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
