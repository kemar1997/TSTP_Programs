"""
Inheritance in programming is similar to genetic inheritance. In genetic inheritance, you inherit attributes like eye
color from your parents. Similarly, when you create a class, it can inherit methods and variables from another class.
The class that is inherited from is the parent class, and the class that inherits is the child class. In this section,
you will model shapes using inheritance. Here is a class that models a shape:
"""


class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}
              """.format(self.width,
                         self.len))


my_shape = Shape(20, 25)
my_shape.print_size()


"""
With this class, you can create Shape objects with width and len. In addition, Shape objects have the method 
print_size, which prints their width and len.

You can define a child class that inherits from a parent class by passing the name of the parent class as a parameter to
the child class when you create it. The following example creates a Square class that inherits from the Shape class:
"""


# class Square(Shape):
#     pass
#
#
# a_square = Square(20,20)
# a_square.print_size()

# >> 20 by 20


"""
Because you passed the Shape class to the Square class as a parameter; the Square class inherits the Shape class's
variables and methods. The only suite you defined in the Square class was the keyword pss, which tells Python not to do
anything.

Because of inheritance, you can create a Square object, pass it a width and length, and call the method print_size on it
without writing any code (aside from pass) in the Square class. This reduction in code is important because avoiding 
repeating code makes your program smaller and more manageable.

A child class is like any other class; you can define methods and variables in it without affecting the parent class:
"""


# class Square(Shape):
#     def area(self):
#         return self.width * self.len
#
#
# a_square = Square(20, 20)
# print(a_square.area())


"""
When a child class inherits a method from a parent class, you can override it by defining a new method with the same
name as the inherited method. A child class's ability to change the implementation of a method inherited from its parent
class is called method overriding.
"""


class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("""I am {} by {}
              """.format(self.width,
                         self.len))

a_square = Square(20, 20)
a_square.print_size()
