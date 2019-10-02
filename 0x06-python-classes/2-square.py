#!/usr/bin/python3
class Square:
    """Simple square class with his size as a field"""

    def __init__(self, size=0):
        """ Instance the class Square
            Arguments:
                @size: the size of every side of the Square,
                        it must be a positive integer value"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
