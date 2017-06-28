from abc import ABCMeta, abstractmethod

"""
Abstraction is the process of "taking away or removing characteristics from something in order to 
reduce it to a set of essential characteristics." You use abstraction in object-oriented programming
when you model objects using classes and omit unnecessary details.

Say you are modeling a person. A person is complex: they have a hair color, eye color, height,
weight, ethnicity, gender, and more. If you create a class to represent a person, some of these
details may not be relevant to the problem you are trying to solve. An example of abstraction is
creating a Person class, but omitting some attributes a person has, like an eye color and height.
The Person objects your class creates are abstractions of people. It is a representation of a 
person stripped down to only the essential characteristics necessary for the problem you are solving.
"""


# Example

class BaseClass(object):
    __metaclass__ = ABCMeta

    # decorator - Way of altering functions or classes
    # without having to inherit or subclass
    @abstractmethod
    def printham(self):
        pass


class InClass(BaseClass):
    def printham(self):
        print("ham")

x = InClass()
x.printham()
