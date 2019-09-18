#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if int(idx) < 0 or int(idx) > len(my_list):
        return my_list
    response = my_list[:]
    response[idx] = element
    return response
