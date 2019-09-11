#!/usr/bin/python3
def uppercase(string):
    for i in string:
        char_value = ord(i)
        if char_value >= 97 and char_value <= 122:
            char_value -= 32
        print("{:s}".format(chr(char_value)), end="")
    print()
