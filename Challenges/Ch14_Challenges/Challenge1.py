"""
1. Add a square_list class variable to a class called Square so that every time you create a new Square object, the new
object gets added to the list.
"""


class Square:
    square_list = []

    def __init__(self):
        self.square_list.append(self)


s1 = Square()
s2 = Square()
s3 = Square()

print(Square.square_list)
