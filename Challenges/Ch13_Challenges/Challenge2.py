"""
2. Define a method in you Square class called change_size that allows you to pass in a number that increases or 
decreases (if the number is negative) each side of a Square object by that number
"""


class Square:
    def __init__(self, a):
        self.side = a

    def change_size(self, n):
        self.side += n

    def calculate_perimeter(self):
        return 4 * self.side


squ = Square(15.6)
print("Square Perimeter: " + str(squ.calculate_perimeter()))

squ.change_size(-2.3)
print("New Square Perimeter: " + str(squ.calculate_perimeter()))
