#!/usr/bin/python3
"""Simple module that stores a Square class that implements or
inherites the Base class for manage the id and representation to JSON
and inherites the Rectangle class for its internal logic.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Simple Square class with a size as width and height, 2D Position
    reference and also it has input validation.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiate a Square with certain dimmensions:

        Arguments:
            size {int}  --  The dimmensions of the new Square.

        Keyword Arguments:
            x {int} --  The coordinate in the X axis of a square
                        in a 2D space(default: {0}).

            y {int} --  The coordinate in the Y axis of a square
                        in a 2D space(default: {0}).

            id {int} -- The integer number that represent the object
                        among other base objects (default: {None}).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The size of the Square which is an integer value bigger than 0.

            Raises:
                TypeError:  When the value passed to the setter isn't an
                            integer.
                ValueError: When the value passed to the setter is less than or
                            equal to 0.
        """
        return super().width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Generates a human readable string that represents the Square.

        Returns:
            {str} --    The string representation of the Square with its
                        attributes.
        """
        base = "[Square] ({}) {}/{} - {}"
        return (base.format(self.id, self.x, self.y, self.height))

    def update(self, *args, **kwargs):
        """Updates certain fields of the instance,
        which are specified by args or kwargs.

        Arguments:
            Args and Kwargs:
                id {int}        --  The integer value that represents the new
                                    id of the instance.
                size {int}      --  The integer value that represents the new
                                    size of the instance.
                x {int}         --  The integer value that represents the new X
                                    coordinate of the instance.
                y {int}         --  The integer value that represents the new
                                    Y coordinate of the instance.
        """
        actual = [self.id, self.size, self.x, self.y]
        if args:
            new_args = list(args[:len(args)]) + actual[len(args):]
        if not args:
            parsed_kwargs = [
                kwargs.get('id'),
                kwargs.get('size'),
                kwargs.get('x'),
                kwargs.get('y')
            ]
            new_args = [
                parsed_kwargs[i] if parsed_kwargs[i] is not None else actual[i]
                for i in range(len(actual))
            ]
        if args or kwargs:
            (self.id, self.size, self.x, self.y) = new_args

    def to_dictionary(self):
        """Creates a dictionary that represents a Square with all its
        attributes.

        Returns:
            {dict} -- A dictionary with all the internal data of a Square.
        """
        dictionary = {'id': self.id, 'size': self.size,
                      'x': self.x, 'y': self.y}
        return dictionary
