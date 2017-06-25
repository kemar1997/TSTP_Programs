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


class Orange:
	def __init__(self, w, c):
		self.weight = w
		self.color = c
		print("Created!")
