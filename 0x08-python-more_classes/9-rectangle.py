#!/usr/bin/python3
"""Simple module that contains a Rectangle class with dimmensions.

It contains the basic geometry logic of a rectangle and his properties are
managed by the getters and setters-
"""


class Rectangle:
    """Simple Rectangle class with height and width.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiate a Rectangle with certain dimmensions:

        Arguments:
            width {int}     --  The width of the new Rectangle (default: {0})
            height {int}    --  The height of the new Rectangle (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """The width of the Rectangle which is an integer value bigger than 0

            Raises:
            TypeError:  When the value passed to the setter isn't an integer.
            ValueError: When the value passed to the setter is less than or
                        equal to zero.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """The height of the Rectangle which is an integer value bigger than 0

            Raises:
            TypeError:  When the value passed to the setter isn't an integer.
            ValueError: When the value passed to the setter is less than or
                        equal to zero.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Computes the Area of a Rectangle.
        Based on the formula AreaRectangle = Height * Width

        Returns:
            {int} -- The integer value of the Rectangle's Area.
        """
        return self.height * self.width

    def perimeter(self):
        """Computes the Perimeter of a Rectangle.
        Based on the formula PerimeterRectangle = 2 * (Height + Width)

        Returns:
            {int} -- The integer value of the Rectangle's Perimeter or
                     0 if the width or height of the Rectangle is 0
                     because that will be a line.
        """
        base = self.height + self.width
        return 2 * base if self.width != 0 and self.height != 0 else 0

    def __str__(self):
        """Generates a human readable string that represents the Rectangle

        Returns:
            {str} -- The string representation of the Rectangel using the #
                     character, it represents a 2d rectangle.
        """
        rectangle = ''
        if self.width != 0 and self.height != 0:
            for row in range(self.height):
                rectangle += str(self.print_symbol) * self.width
                rectangle += '\n' if row != self.height - 1 else ''
        return rectangle

    def __repr__(self):
        """Generates an internal representation of the Rectangle.

        Returns:
            {str} -- The string that is the internal representation of the
                     Rectangle and can be used with eval().
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Handle the deletion of an instance printing an exit message.
        """
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Checks the biggest Rectangle based on the Area.

        Arguments:
            rect_1 {Rectangle} -- The first Rectangle to compare.
            rect_2 {Rectangle} -- The second Rectangle to compare.

        Raises:
            TypeError:  If rect_1 or rect_2 aren't instance of the class
                        Rectangle.

        Returns:
            [Rectangle] --  The biggest rectangle between rect_1 and rect_2
                            or rect_1 in the case that they have the same Area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates an instance of Rectangle which is a square (width == height)
        based on a specific size.

        Keyword Arguments:
            cls {class} --  The class of the object that is calling the
                            function, which may be Rectangle by default or a
                            subclass.
            size {int}  --  The size of the new square, which is a Rectangle
                            with the same height and width (default: {0})

        Returns:
            Rectangle   -- The new Rectangle with size as his height and width.
        """
        return cls(size, size)
