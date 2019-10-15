#!/usr/bin/python3
"""Simple module with a class that inherits list.
"""


class MyList(list):
    """Simple list class with ordered print method.
    """

    def __init__(self):
        """Initialize a MyList object using the init method of the list object.
        """
        super().__init__()

    def print_sorted(self):
        """Prints the elements of the list in an ascending sorted order.
        """
        print(sorted(self))
