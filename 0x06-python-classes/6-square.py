#!/usr/bin/python3
class Square:
    """Simple square class with his size as a field"""

    def __init__(self, size=0, position=(0, 0)):
        """ Instance the class Square
            Arguments:
                @size: the size of every side of the Square,
                        it must be a positive integer value"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not self.__is_a_valid_position(position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        """ Getter for the field size as a property
            Return:
                    Value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for the field size as a property.
            Arguments:
                @value: the value of size
                        that must be a positive integer value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Getter for the field position as a property
            Return:
                    Value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter for the field position as a property.
            Arguments:
                @value: the value of position
                        that must be a tuple of two positive integer values."""
        if self.__is_a_valid_position(value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Compute the area of a square
            with the formula:
                                area = @size ^ 2 = @size * @size
            Return:
                    Power of the Square size to 2 or
                    size multiplicated by size."""
        return self.__size ** 2

    def my_print(self):
        """ Prints a square using the character # in the standard output
            or a blank line if @size is 0
            and adjust it with spaces in the X and Y axis
            based on the @position values"""
        if not self.size:
            print()
        else:
            for spaces_Y in range(self.position[1]):
                print()
            for row in range(self.size):
                for spaces_X in range(self.position[0]):
                    print(" ", end="")
                for row in range(self.size):
                    print("#", end="")
                print()

    def __is_a_valid_position(self, positions):
        """ Check if a value can be a position by checking
            if @positions is a tuple of exactly two positive integers
            Return:
                    True if @positions is a valid position field
                    False otherwise"""
        if type(positions) is tuple\
                and len(positions) == 2\
                and type(positions[0]) is int\
                and type(positions[1]) is int\
                and positions[0] >= 0\
                and positions[1] >= 0:
            return True
        else:
            return False
