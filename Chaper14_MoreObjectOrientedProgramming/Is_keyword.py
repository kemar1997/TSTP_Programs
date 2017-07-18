# The keyword is returns True if two objects are the same object, and False if not:


class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)


another_bob = Person()
print(bob is another_bob)

"""
When you use the keyword 'is' in an expression with the objects bob and same_bob as operators, the expression evaluates
to True because both variables point to the same Person object. When you create a new Person object and compare it to 
the original bob, the expression evaluates to False because the variable point to different Person objects.
"""

# Use the is keyword to check if a variable is None:

x = 10
if x is None:
    print("x is None :( ")
else:
    print("x is not None")

x = None
if x is None:
    print("x is None")
else:
    print("x is None :( ")
