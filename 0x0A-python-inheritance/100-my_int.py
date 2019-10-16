#!/usr/bin/python3
"""Simple module that contains a class that inherits of int
with equality operators inversed.
"""


class MyInt(int):
    """Simple class that inherites int with special equality operators.
    """

    def __eq__(self, other):
        """Inversed equality operator (overload magic method).

        Arguments:
            other {MyInt}   --  the object that will be compared with our
                                internal MyInt.

        Returns:
            bool    --  True if self value is not equal with other,
                        False otherwise.
        """
        return self.__int__() != other.__int__()

    def __ne__(self, other):
        """Inversed not equality operator (overload magic method).

        Arguments:
            other {MyInt}   --  the object that will be compared with our
                                internal MyInt.

        Returns:
            bool    --  True if self value is equal with other,
                        False otherwise.
        """
        return self.__int__() == other.__int__()
