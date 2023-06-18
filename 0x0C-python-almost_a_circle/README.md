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

* [models](folder/models.extension) folder containing all the classes and corresponding subclass
* [base.py](models/base.py) - Contains the base class `Base` for all other classe:
* Private class attribute `__nb_objects = 0.`
* Public instance attribute `id.`
* Class constructor `def __init__(self, id=None):`
  - If `id` is `None,`  increments` __nb_objects` and assigns its value to the public instance attribute `id.`
  - Otherwise, sets the public instance attribute id to the provided `id.`
