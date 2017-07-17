"""
Now that you've learned about the four pillars of object-oriented programming. I am going to cover one more important
concept: composition. Composition models the "has a" relationship by storing an object as a variable in another object.
For example, you can use composition to represent the relationship between a dog and its owner (a dog has a owner).
To model this, first you define classes to represent dogs and people:
"""


class Dog():
    def __init__(self,
                 name,
                 breed,
                 owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Person():
    def __init__(self, name):
        self.name = name

"""
Then, when you create a Dog object, you pass in a Person object as the owner parameter:
"""

mick = Person("Mick Jagger")
stan = Dog("Stanley",
           "Bulldog",
           mick)
print(stan.owner.name)

"""
Now the stan object "Stanley" has an owner - a Person object named "Mick Jagger" - stored in the owner instance
variable.
"""