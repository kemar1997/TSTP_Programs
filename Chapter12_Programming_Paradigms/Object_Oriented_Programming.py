"""
The object-oriented programming paradigm also addresses the problems that arise in procedural programming by eliminating global state, but instead of storing
 state in functions, it is stored in objects. In object-oriented programming, classes define a set of objects that can interact with each other. Classes are a
 mechanism for the programmer to classify and group together similar objects. Think of a bag of oranges. Each orange is an object. All oranges have the same
 attributes, such as color and weight, but the values of these attributes vary from one orange to the next. You can use a class to model oranges and create
 orange objects with different values. For instance, you can define a class that allows you to create an orange object that is dark orange and weighs 10 oz,
 and an orange object that is light orange and weighs 12 oz.

Every object is an instance of a class. If you define a class called Orange, and create two Orange objects, each one is an instance of the class Orange; they
have the same data type; Orange. You can use the terms object and instance interchangeably. When you define a class, all of the instances of that class will
be similar: They all have the attributes defined in the class thay are an instance of, such as color or weight for a class representing an orange; but each
instance can have different values for these attributes.

In Python, a class is a compound statement with a header and suites. You define a class with the syntax class [name]: [suites] where [name] is the name of the
class and [suites] are the class' suites you define. By convention, classes in Python always start with a capital letter, and you write them in camelCase; which
means if a class name has more than one word, the first letters of all the worlds should be capitalized LikeThis, instead of separated by an underscore (the 
convention for function names). A suite in a class can be a simple statement or a compound statement called a method. Methods are like functions, but you define
them inside of a class, and you can only call them on the object the class creates. Method names, like function nmes, should be all lowercase with words 
separated by underscores.

You define methods with the same syntax as functions, with two differences: you must define a method as a suite in a class, and it has to accept at least one
parameter (except in special cases). By convention, you always name the first parameter of a method self. You have to define at least one parameter when you 
create a method, because when you call a method on an object, Python automatically passes the object that called the method to method as a parameter:
"""

# class Orange:
	# def __init__(self):
		# print("Created!")

		
"""
You can use self to define an instance variable: a variable that belongs to an object. If you create multiple objects, they can all have different instance
variable values. You can define instance variables with the syntax self.[variable_name] = [variable_value]. You normally define instance variables inside of a
special method called __init__ (which stands for initialize) that Python calls when you create an object:
"""

# Here is an example of a class that represents an orange:


# class Orange:
	# def __init__(self, w, c):
		# self.weight = w
		# self.color = c
		# print("Created!")
		
"""
The code in __init__ executes when you create an Orange object and creates two instance variables: weight and color. You can use these variables like regular
variables, in any method in your class. When you create and Orange object, the code in __init__ also prints  Created! Any method surrounded by double 
underscores, like __init__, is called a magic method: a method Python uses for special purposes like creating an object.

You can create a new Orange object with the same syntax you use to call a function; [classname]([parameters]), replacing [classname] with the name of the class
you want to use to create the object and replacing [parameters] with the parameters __init__ accepts. You do not have to pass in self; Python passes it in
automatically. Creating a new object is called instantiating a class:
"""

##class Orange:
##	def __init__(self, w, c):
##		self.weight = w
##		self.color = c
##		print("Created!")
##		
##
##or1 = Orange(10, "dark orange")
##print(orl)


"""
After the class definition, you instantiate the Orange class with the code Orange(10, "dark orange") and Created! prints. Then, you print the Orange object itself,
and Python tells you it is an Orange object and gives you its location in memory.

Once you've created an object, you can get the value of its instance variables with the syntax [object_name].[variable_name]:
"""


class Orange():
        def __init__(self, w, c):
                """weights are in oz"""
                self.weight = w
                self.color = c
                self.mold = 0
                print("Created!")

        # giving the Orange object the ability to rot
        def rot(self, days, temp):
                self.mold = days * temp

or1 = Orange(10, "dark orange")
##print(or1.weight)
##print(or1.color)

# You can change the value of an instance variable with the syntax [object_name].[variable_name] = [new_value]:

or1.weight = 100
or1.color = "changed to light orange"
print(or1.weight)
print(or1.color)

"""
Although the instance variables color and weight started with the values "dark orange" and 10, you were able to change to change their values.

You can use the Orange class to create multiple oranges:
"""


##or2 = Orange(4, "Light Orange")
##or3 = Orange(8, "Dark Orange")
##or4 = Orange(14, "Yellow")

"""
There is more to an orange than its physical properties, like color and weight. Oranges also do things, like rot, that you can model with methods.
Here is how you can give an Orange object the ability to rot:
"""

orange = Orange(6, "orange")
print(orange.mold)
orange.rot(10, 98)
print(orange.mold)

"""
The method rot accepts two parameters: the number of days since someone picked the orange, and the average temp during that time. When you call it,
the method uses a formula to increment the instance variable mold, which works because you can change the value of any instance variable inside of
any method. Now, the orange can rot.

You can  define multiple methods in a class. Here is an example of modeling a rectangle with a method to calculate its area, and another method to
change its size:
"""

class Rectangle():
        def __init__(self, w, l):
                self.width = w
                self.len = l

        def area(self):
                return self.width * self.len

        def chng_sz(self, w, l):
                self.width = w
                self.len = l


rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.chng_sz(20, 40)
print(rectangle.area())

"""
In this example, Rectangle objects have two instance variables: len and width. The area method returns the area of the Rectangle object by multiplying
the instance variables together, and the chng_sz method changes them by assigning them to numbers the caller passes in as parameters.

Object-oriented programming has several advantages. It encourages code reuse, and thus decreases the amount of time spent developing and maintaining
code. It also encourages breaking problems up into multiple pieces, which results in code that is easy to maintain. A disadvantage of object-oriented
programming is that creating programs takes extra effort because a great deal of planning is often involved in designing them.
"""
