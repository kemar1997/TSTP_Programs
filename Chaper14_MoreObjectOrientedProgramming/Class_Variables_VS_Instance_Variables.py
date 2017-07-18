"""
In Python, classes are objects. This idea comes from Smalltalk, an influential programming language that pioneered
object-oriented programming. Each class in Python is an object that is an instance of class "type":
"""


class Square:
    pass


print(Square)

# In this example, the class Square is an object, and you printed it.

"""
Classes have two types of variables: class variables and instance variables. The variables you've seen so far have been
instance variables, defined with syntax self.[variable_name] = [variable_value]. Instance variables belong to objects:
"""


class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}
              """.format(self.width,
                         self.len))


my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()

# In this example, width and len are instance variables.

"""
Class variables belong to the object Python creates for each class definition and the objects they create. You define
class variables like regular variables (but you must define them inside of a class). You can access them with class
objects, and with an object created with a class object. You access them the same way you access instance variables
(preceding the variable name with self.). Class variables are useful; they allow you to share data between all of the
instances of a class without relying on global variables:
"""


class RectangleTwo:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width,
                          self.len))

    def print_size(self):
        print("""{} by {}
              """.format(self.width,
                         self.len))

r1 = RectangleTwo(10, 24)
r2 = RectangleTwo(20, 40)
r3 = RectangleTwo(100, 200)

print(RectangleTwo.recs)

"""
In this example, you added a class variable called recs to the Rectangle class. You defined outside of the __init__
method because Python ony calls the __init__ method when you create an object, and you want to be able to access the 
class variable using the class object (which does not call the __init__ method).

Next, you created three Rectangle objects. Each time a Rectangle object is created, the code in the __init__ method
appends a tuple containing the width and length of the newly created object to the recs list. With this code, whenever 
you create a new Rectangle object, it is automatically added to the recs list. By using a class variable, you were able
to share data between the different objects created by a class, without having to use a global variable. 
"""
