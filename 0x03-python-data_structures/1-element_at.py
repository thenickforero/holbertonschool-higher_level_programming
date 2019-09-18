#!/usr/bin/python3
def element_at(my_list, idx):
    if int(idx) < 0 or int(idx) + 1 > len(my_list):
        return None
    return my_list[idx]
