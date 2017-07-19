"""
3. Write a function that takes two objects as parameters and returns True if they are the same object, and False if not.
"""


class Dog:
    def __init__(self):
        self.name = 'Bella'

# Returns True
bella = Dog()
same_dog = bella
print(same_dog is bella)

# Returns False
different_dog = Dog()
print(different_dog is bella)
