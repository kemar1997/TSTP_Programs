from math import pi

# Create a Circle class with a method called area that calculates and returns its
# area. Then create a Circle object, call area on it, and print the result.

# A = pi * r^2 (Just a reference)

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return pi * self.radius**2


circle = Circle(23)
print(circle.area())
