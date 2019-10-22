#!/usr/bin/python3
"""Simple module that stores a Rectangle class that implements or
inherites the Base class for manage the id and representation to JSON.
"""


from models.base import Base


class Rectangle(Base):
    """Simple Rectangle class with width, height and 2D Position reference,
    also it has input validation.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate a Rectangle with certain dimmensions:

        Arguments:
            width {int}     --  The width of the new Rectangle.
            height {int}    --  The height of the new Rectangle.

        Keyword Arguments:
            x {int} --  The coordinate in the X axis of a rectangle
                        in a 2D space(default: {0}).

            y {int} --  The coordinate in the Y axis of a rectangle
                        in a 2D space(default: {0}).

            id {int} -- The integer number that represent the object
                        among other base objects (default: {None}).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The width of the Rectangle which is an integer value bigger than 0.

            Raises:
                TypeError:  When the value passed to the setter isn't an
                            integer.
                ValueError: When the value passed to the setter is less than or
                            equal to 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """The height of the Rectangle which is an integer value bigger than 0.

            Raises:
                TypeError:  When the value passed to the setter isn't an
                            integer.
                ValueError: When the value passed to the setter is less than or
                            equal to 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """The coordinate in the X axis of the Rectangle
        which is an integer value bigger or equal to 0.

            Raises:
                TypeError:  When the value passed to the setter isn't an
                            integer.
                ValueError: When the value passed to the setter is less than 0.
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """The coordinate in the Y axis of the Rectangle
        which is an integer value bigger or equal to 0.

            Raises:
                TypeError:  When the value passed to the setter isn't an
                            integer.
                ValueError: When the value passed to the setter is less than 0.
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        """Verify if value is a valid integer value.

        Arguments:
            name {str}      --  a string related with the value.
            value {object}  --  the value that will be checked.

        Raises:
            TypeError:  if value is not an integer.
            ValueError: if value is an integer less or equal to 0.
        """
        if name is not None and len(name) > 0:
            if type(value) is not int:
                raise TypeError('{:s} must be an integer'.format(name))
            if value <= 0 and name in ('width', 'height'):
                raise ValueError('{:s} must be > 0'.format(name))
            if value < 0 and name in 'xy':
                raise ValueError('{:s} must be >= 0'.format(name))

    def area(self):
        """Computes the Area of a Rectangle.
        Based on the formula AreaRectangle = Height * Width

        Returns:
            {int} -- The integer value of the Rectangle's Area.
        """
        return self.height * self.width

    def display(self):
        """Prints a representation of the rectangle in a 2D space
        using the # character.
        """
        print('\n' * self.y, end='')
        for row in range(self.height):
            print("{:s}{:s}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        """Generates a human readable string that represents the Rectangle.

        Returns:
            {str} --    The string representation of the Rectangle with its
                        attributes.
        """
        base = '[Rectangle] ({}) {}/{} - {}/{}'
        return (base.format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Updates certain fields of the instance,
        which are specified by args or kwargs.

        Arguments:
            Args and Kwargs:
                id {int}        --  The integer value that represents the new
                                    id of the instance.
                width {int}     --  The integer value that represents the new
                                    width of the instance.
                height {int}    --  The integer value that represents the new
                                    height of the instance.
                x {int}         --  The integer value that represents the new X
                                    coordinate of the instance.
                y {int}         --  The integer value that represents the new
                                    Y coordinate of the instance.
        """
        actual = [self.id, self.width, self.height, self.x, self.y]
        if args:
            new_args = list(args[:len(args)]) + actual[len(args):]
        if not args:
            parsed_kwargs = [
                kwargs.get('id'),
                kwargs.get('width'),
                kwargs.get('height'),
                kwargs.get('x'),
                kwargs.get('y')
            ]
            new_args = [
                parsed_kwargs[i] if parsed_kwargs[i] is not None else actual[i]
                for i in range(len(actual))
            ]
        if args or kwargs:
            (self.id, self.width, self.height, self.x, self.y) = new_args

    def to_dictionary(self):
        """Creates a dictionary that represents a Rectangle with all its
        attributes.

        Returns:
            {dict} -- A dictionary with all the internal data of a Rectangle.
        """
        dictionary = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return dictionary
