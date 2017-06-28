"""
Encapsulation refers to two concepts. The first is that in object-oriented
programming, objects group variables (state) and methods (for altering state or
doing calculations that use state) in a single unit - the object:
"""


class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

"""
In this case, the instance variables len and width hold the object's state. The
object's state is grouped in the same unit (the object) as the method area. The
method uses the object's state to return the rectangle's area.

The second concept, encapsulation, refers to hiding a class's internal data to
prevent the "client", the code outside the class that uses the object, from
directly accessing it:
"""


# class Data:
#    def __init__(self):
#        self.nums = [1, 2, 3, 4, 5]


#    def change_data(self, index, n):
#        self.nums[index] = n


"""
The class Data has an instance variable called nums that contains a list of
integers. Once you create a Data object, there are two ways you can change the
items in nums: by using the change_data method, or by directly accessing the
nums instance variable using the Data object:
"""


class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n


data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)


data_two = Data()
data_two.change_data(0, 600)
print(data_two.nums)


"""
Both ways of changing an item in the nums instance variable work, but what
happens if you decide to make the variable nums a tuple instead of a list? If
you make this change, any client code trying to alter the items in the variable
nums, like you did with nums[0] = 100, will no longer work, because tuples are
immutable.

Many programming languages solve this problem by allowing programmers to define
private variables and private methods: variables and methods that objects can
access in the code that implements the various methods, but the client cannot.
Private variables and methods are useful when you have a method or variable
that your class uses internally, but you plan to change the implementation of
your code later (or you want to preserve the flexibility of that option), and
thus don't want whoever is using the class to rely on them because they might
change (and would then break the client's code). Private variables are an
example of the second concept encapsulation refers to; private variables hide a
class's internal data to prevent the client from directly accessing it. Public
variables, on the other hand, are variables a client can access.

Python does not have private variables. All of Python's variables are public.
Python solves the problem private variables address another way - by using
naming conventions. In Python, if you have a variable or method the caller
should not access, you precede its name with an underscore. Python programmers
know if the name of a  method or variable starts with an underscore, they
shouldn't use it (although they are still able to at their own risk):
"""


class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        # clients can use this
        pass

    def _unsafe_method(self):
        # clients shouldn't use this
        pass


"""
Client programmers reading this code know the variable self.public is safe to
use, but they shouldn't use the variable self._unsafe because it starts with an
underscore, and if they do, they do so at their own risk. The person maintaining
this code has no obligation to keep the variable self._unsfe around, because
callers are not supposed to be accessing it. Client programmers know the method
public_method is safe to use, whereas the method _unsafe_method is not, because
its name starts with an underscore.
"""
