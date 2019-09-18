#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    response = my_list[:]
    if int(idx) < 0 or int(idx) > len(my_list):
        return response
    response[idx] = element
    return response
