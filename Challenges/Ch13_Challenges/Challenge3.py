"""
3. Create a class called Shape. Define a method in it called what_am_i that prints "I am a shape" when called. Change 
your Square and Rectangle classes from the previous challenges to inherit from Shape, create Square and Rectangle 
objects, and call the new method on both of them.
"""


class Shape:
    def what_am_i(self):
        print("I am a shape.")


class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)


class Square(Shape):
    def __init__(self, a):
        self.side = a

    def calculate_perimeter(self):
        return 4 * self.side


rec = Rectangle(5, 2)
squ = Square(15.6)
rec.what_am_i()
squ.what_am_i()
print("Rectangle Perimeter: " + str(rec.calculate_perimeter()))
print("Square Perimeter: " + str(squ.calculate_perimeter()))
