#!usr/bin/python3

"""
Define a base model class
serves as a foundation or blueprint for specialized classes. 
It provides a way to organize and structure related classes in a hierarchy.
"""


class Base:
    """ This class will be the “base” of all other classes in this project. 

    Attributes:
    __nb_objects (int): is used as a private class attribute to keep track of the number of objects created from the Base class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

