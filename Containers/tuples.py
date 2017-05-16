"""
A tuple is a container that stores objects in a specific order. Unlike lists, tuples
are immutable, which means their contents cannot change. Once you create a tuple, you
cannot modify the value of any of the items in it, add new items to it, or remove
items from it. You represent tuples with parentheses. You must separate items in a
tuple with commas. There are two syntaxes to create a tuple:
"""

# my_tuple = tuple()
# print(my_tuple)

# And:

# my_tuple = ()
# print(my_tuple)

"""
To add objects to a tuple, create one with the second syntax with each item you want
to add, separating them with commas:
"""

# rndm = ("M. Jackson", 1958, True)
# print(rndm)

"""
Even if a tuple only has one item in it, you need to put a comma after it. That
way, Python can differentiate it from a number surrounded by parentheses that
denote its position in the order of operations:
"""

# this is a tuple
# my_tuple = ("self_taught",)
# print(my_tuple)

# this is not a tuple
# result = (9) + 1
# print(result)

"""
You cannot add new item to a tuple or chage it once you've created it. If you try
to change an object in a tuple after you've created it, Python will raise an 
exception:
"""

# dys = ("1984",
#        "Brave New World",
#        "Fahrenheit 451")

# dys[1] = "Handmaid's Tale"
# TypeError: 'tuple' object does not support item assignment

"""
You can get items from tuple the same way you would from a list - by referencing the
item's index:
"""

dys = ("1984",
       "Brave New World",
       "Fahrenheit 451")

print(dys[2])