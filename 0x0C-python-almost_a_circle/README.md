# :eagle: 0x0C-python-almost_a_circle :eagle:

I have practice:

* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file 
* What is args and how to use it
* What is `kwargs` and how to use it
* How to handle named arguments in a function

The following function tools were used in creating all the classes and testing its functionality:
* Import
* Exceptions
* Class
* Private attribute
* Getter/Setter
* Class method
* Static method
* Inheritance
* Unittest
* Read/Write file
* args/kwargs
* JSON and CSV
* serialization/deserialization

## Technologies
* Python Scripts are written with Python 3.4.3
* Tested on Ubuntu 14.04 LTS

## Task file descriptions

### classes:

* [models](0x0C-python-almost_a_circle/models.extension) folder containing all the classes and corresponding subclass
* [base.py](models/base.py) - Contains the base class `Base` for all other classe:
* Private class attribute `__nb_objects = 0.`
* Public instance attribute `id.`
* Class constructor `def __init__(self, id=None):`
  - If `id` is `None,`  increments` __nb_objects` and assigns its value to the public instance attribute `id.`
  - Otherwise, sets the public instance attribute id to the provided `id.`
* [rectangle.py](models/rectangle.py) - Contains the class Rectangle, a subclass inheritance of `Base`:
* private instance attribut `__width`, `__height`, `__x`, and `__y`.
  - Each privatr instance attribute featurring its own getter/setter.
* class constructor `def__init__(self, width,height, x=0, y=0, id=None)`:
  - if either of the `width`, `h`eight`,`x` or `y`is not an integer, raises a `TypeError` exception with the message `<attribute> must be an integer`.
  - If either of `width` or `height` is >= 0, raises a `ValueError` exception with the message `<attribute> must be > 0`.
  - If either of `x` or `y` is less than 0, raises a `ValueError` exception with the message `<attribute> must be >= 0`.
* Public method `def area(self)`: that returns the area of the `Rectangle` instance.
* Public method `def display(self)`: that prints the `Rectangle` instance to `stdout` using the `#` character.
  - Prints new lines for the y coordinate and spaces for the `x` coordinate.
* Overwrite of `__str__` method to print a Rectangle instance in the format `[Rectangle] (<id>) <x>/<y>.`
* Public method def update``(self, *args, **kwargs)``: that updates an instance of a `Rectangle` with the given attributes.
  - ``*args`` must be supplied in the following order:
    - 1st: id
    - 2nd: width
    - 3rd: height
    - 4th: x
    - 5th: y
  - ``**kwargs`` is expected to be a double pointer to a dictionary of new key/value attributes to update the `Rectangle` with.
  - ``**kwargs`` is skipped if ``*args`` exists.
* Public method def to_dictionary(self): that returns the dictionary representation of a` Rectangle` instance.
