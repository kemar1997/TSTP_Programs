"""
Every class in Python inherits from a parent class called Object. Python utilizes the methods inherited from Object in
different situations - like when you print an object:
"""


class Lion:
    def __init__(self, name):
        self.name = name

lion = Lion("Dilbert")
print(lion)

"""
When you print a Lion object, Python calls a magic method called __repr__ it inherited from Object on it, and prints
whatever the __repr__ method returns. You can override the inherited __repr__ method to change what prints:
"""


class LionTwo:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

lion1 = LionTwo("Dilbert")
print(lion1)

"""
Because you overrode the __repr__ method inherited from Object and changed it to return the Lion object's name, when you
print a Lion object, its name - in this case, Dilbert - prints instead of something like <__main__.Lion object at 0x026D
26B0> that the __repr__ method would have returned.

Operands in an expression must have a magic method the operator can use to evaluate the expression. For example, in the
expression 2 + 2, each integer object has a magic method called __add__ that Python calls when it evaluates the 
expression. If you define an __add__ method in a class, you can use the objects it creates as operands in an expression
 with the addition operator:
"""


class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n +
                   other.n)

x = AlwaysPositive(-30)
y = AlwaysPositive(17)

print(x + y)

"""
AlwaysPositive objects can be used as operands in an expression with the addition operator because you defined the 
__add__ method. When Python evaluates an expression with an addition operator, it calls the method __add__ on the first 
operand object, passes the second operand object into __add__ as a parameter, and returns the result.

In this case, __add__ uses the built-in function abs to return the absolute value of two numbers added together in an
expression. Because you defined __add__ this way, two AlwaysPositive objects evaluated in an expression with the 
addition operator will always return the absolute value of the sum of the two objects; thus, the result of the 
expression is always positive.
"""
