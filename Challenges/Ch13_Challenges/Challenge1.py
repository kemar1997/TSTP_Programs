"""
1. Create Rectangle and Square classes with a method called calculate_perimeter that calculates the perimeter of
the shapes they represent. Create Rectangle and Square objects and call the method on both of them.
"""


class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)


class Square:
    def __init__(self, a):
        self.side = a

    def calculate_perimeter(self):
        return 4 * self.side


rec = Rectangle(5, 2)
squ = Square(15.6)
print("Rectangle Perimeter: " + str(rec.calculate_perimeter()))
print("Square Perimeter: " + str(squ.calculate_perimeter()))
