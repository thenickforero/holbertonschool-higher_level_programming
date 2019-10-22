#!/usr/bin/python3
"""Simple Base module that contains an abstract class for managing diverse
objects and transform its representation.

It contains the base logic for handle id's for every instance created an to
handle the bidirectional representation of every object in a JSON format.
"""
import json
import turtle
import random


class Base:
    """Simple Base class with handlers for create and update instances,
    also enables the feature of save an create instances from/to JSON files.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate a Base object and assings it's an automatic ID,
        based of number on the number of Base instances created,
        if isn't specificated.

        Keyword Arguments:
            id {int} -- The integer number that represent the ID
                        of a certain instance of base (default: {None})
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Translate a list of instance dictionaries to a JSON formatted
        string.

        Arguments:
            list_dictionaries {list[dict]}  --  The list with dictionaries of
                                                Base object instances
                                                (with its properties)
                                                that will be processed.

        Returns:
            {str}   --  A JSON formatted string that represents the list of
                        instances.
        """
        if not list_dictionaries:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of instance objects in a JSON formatted file.

        Arguments:
            list_objs {list[dict]}  --  The list with dictionaries of
                                        Base object instances
                                        (with its properties)
                                        that will be processed.
        """
        with open('{}.json'.format(cls.__name__), 'w') as file:
            if not list_objs:
                file.write(cls.to_json_string([]))
            else:
                instances_list = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(instances_list))

    @staticmethod
    def from_json_string(json_string):
        """Parses a JSON formatted string to a list of its python
        representation.

        Arguments:
            json_string {str}   --  The JSON formatted string that will be
                                    processed.

        Returns:
            {list[dict]}  --    The list with dictionaries of
                                Base object instances
                                (with its properties).
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of a certain Base subclass and fill it with
        specific values for its fields.

        Returns:
            {cls}   --  The new instance of a @cls initialized with the values
                        stored in @dictionary.
        """
        if cls.__name__ == 'Rectangle':
            response = cls(1, 1, 0, 0)
        if cls.__name__ == 'Square':
            response = cls(1, 0, 0)
        response.update(**dictionary)
        return response

    @classmethod
    def load_from_file(cls):
        """Creates a list of Base subclass objects
        based on the content of a JSON formatted file.

        Returns:
            {list[cls]}     --  The list with the instances of the objects
                                stored in the JSON file.
        """
        try:
            with open('{}.json'.format(cls.__name__), 'r') as file:
                data = file.read()
                json_data = cls.from_json_string(data)
                list_instances = [cls.create(**ins) for ins in json_data]
                return list_instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Prints a rectangle in a turtle canvas.

        Arguments:
            list_rectangles {list[Rectangle]}   --  A list with Rectangles
                                                    to print.
            list_squares {list[Square]}         --  A list with Squares
                                                    to print.
        """
        def draw_figure(x, y, width, height):
            """Helper function to print any figure.
            """
            color = ('green', 'blue', 'yellow',
                     'red', 'black', 'orange', 'pink')
            myPen = turtle.Turtle()
            myPen.shape("turtle")
            myPen.penup()
            myPen.speed(5)
            myPen.goto(x, y)
            myPen.pendown()
            myPen.begin_fill()
            myPen.color(random.choice(color))
            for i in range(4):
                myPen.forward(width if i % 2 == 0 else height)
                myPen.left(90)
            myPen.end_fill()

        for rectangle in list_rectangles:
            draw_figure(rectangle.x, rectangle.y, rectangle.width,
                        rectangle.height)
        for square in list_squares:
            draw_figure(square.x, square.y, square.size, square.size)
