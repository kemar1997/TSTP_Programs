"""
Polymorphism is 'the ability (in programming) to present the same interface for differing underlying forms (data types).
' An interface is a function or a method. Here is an example of presenting the same interface for different data types:
"""

print("Hello, World!")
print(200)
print(200.1)

"""
You presented the same interface, the print function, for three different data types: a string, an integer, and a
floating-point number. You didn't have to define and call three separate functions (like print_string to print strings,
print_int to print integers, and print_float to print floating-point numbers) to print three different data types;
instead, you were able to use the print function to present on interface to print them all.

The built-in function type returns the data type of an object:
"""

print(type("Hello, World"))
print(type(200))
print(type(200.1))

"""
Let's say you want to write a program that creates three objects that draw themselves: triangles, squares, and circles.
You can achieve this goal by defining three different classes: Triangle, Square, and Circle, and defining a method 
called draw for each of them. Triangle.draw() will draw a triangle. Square.draw() will draw a square. And Circle.draw()
will draw a circle. With this design, each of the objects has a draw interface that knows how to draw itself. You 
presented the same interface for three different data types.

If Python did not support polymorphism, you would need a method to draw each shape: perhaps draw_triangle to draw a 
Triangle object, draw_square to draw a Square object, and draw_circle to draw a Circle object.

Also, if you had a list of these objects and you wanted to draw each one, you would have to test each object to get its
type, then call the correct method for that type, making the program larger, harder to read, harder to write, and more
fragile. It also makes the program harder to enhance, because every time you added a new shape to your program, you 
would have to track down every place in the code where you draw the shapes and add a test (to find what method to use)
for that new shape type, plus a call to that new draw function. Here is an example of drawing shapes with and without
polymorphism:
"""


# Do not run

# Drawing shapes
# w/o polymorphism
shapes = [trl, sql, crl]
for a_shape in shapes:
    if type(a_shape) == "Triangle":
        a_shape.draw_triangle()
    if type(a_shape) == "Square":
        a_shape.draw_square()
    if type(a_shape) == "Circle":
        a_shape.draw_circle()


# Drawing shapes
# with polymorphism
shapes = [trl,
          swl,
          crl]
for a_shape in shapes:
    a_shape.draw()


"""
If you wanted to add a new shape to the shapes list without polymorphism, you would have to modify the code in the
for-loop to test a_shape type and call its draw method. With a uniform, polymorphic interface, you can add as many shape
classes to the shapes list in the future as you want, and the shape will be able to draw itself without any additional
code.
"""
