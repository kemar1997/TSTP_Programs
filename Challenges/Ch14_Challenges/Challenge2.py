"""
2. Change the Square class so that when you print a Square object, a message prints telling you the len of each of the
four side of the shape. For example, if you create a square with Square(29) and print it, Python should print 29 by 29
by 29 by 29.
"""


class Square:
    square_list = []

    def __init__(self, side):
        self.s = side
        self.square_list.append(self.s)

    def print_size(self):
        print("""{} by {} by {} by {}
              """.format(self.s,
                         self.s,
                         self.s,
                         self.s))

s1 = Square(29)
s2 = Square(63)
s3 = Square(22)

print(Square.print_size(s3))
