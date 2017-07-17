"""
Create a class called Horse and a class called Rider. Use composition to model a horse that has a rider
"""


class Horse:
    def __init__(self,
                 name,
                 owner):
        self.name = name
        self.owner = owner


class Rider:
    def __init__(self, name):
        self.name = name


john = Rider("John Whitaker")
jaguar = Horse("Jaguar",
               john)
print(jaguar.owner.name)