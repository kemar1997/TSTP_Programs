"""
Dictionaries are another built in container for storing objects. They are used to link one object,
called a key, to another object called the value. Linking one object to another is called mapping.
The result is a key-value pair. You add key-value pairs to a dictionary. You can then look up a key
in the dictionary and get its value. You cannot, however, use a value to look up a key.
"""

"""
Dictionaries are mutable, so you can add new key-value pairs to them. Unlike lists and tuples,
dictionaries do not store objects in a specific order. Their usefulness relies on the associations
formed between keys and values, and there are many situations where you need to store data in pairs.
For example, you could store information about someone in a dictionary. You could map a key called
height to a value representing the person's height, a key called eyecolor to a value representing
the person's eye color and a key called nationality to a value representing the person's
nationality.
"""

# Keys          Values
# 'a'           'alpha'
# 'o'           'omega'
# '9'           'gamma'

"""
Dictionaries are represented with curly brackets. There are two syntaxes for creating dictionaries:
"""

# my_dict = dict()
# print(my_dict)
#
# And:
#
# my_dict = {}
# print(my_dict)

"""
You can add key-value pairs to a dictionary when you create it. Both syntaxes have the key separated
from the value by a colon. A comma must separate each key-value pair. Unlike a tuple, if you have
just one key-value pair, you do not need a comma after it. Here is how you add key-value pairs to
a dictionary when you create it:
"""

# fruits = {"Apple":
#           "Red",
#           "Banana":
#           "Yellow"}
#
# print(fruits)

"""
Dictionaries are mutable. Once you've created a dictionary, you can add key-value pairs to it with
the syntax [dictionary_name][[key]]=[value], and look up a value using a key with the syntax
[dictionary_name][key]:
"""

# facts = dict()


# add a value
# facts["code"] = "fun"
# look up key
# print(facts["code"])


# add a value
# facts["Bill"] = "Gates"
# look up key
# print(facts["Bill"])

# add a value
# facts["founded"] = 1776
# look up key
# print(facts["founded"])

"""
Any object can be a dictionary value. In the previous example, the first two values are strings,
and the last value, 1776, is an integer.

Unlike a dictionary value, a dictionary key must be immutable. A string or a tuple can be a
dictionary key, but not a list or a dictionary.

Use the in keyword to check if a key is in a dictionary. You cannot use the in keyword to check
if a value is in a dictionary:
"""

# bill = dict({"Bill Gates":
#              "charitable"})
#
# print("Bill Gates" in bill)

"""
If you try to access a key that isn't in a dictionary, Python will raise an exception.

Add the keyword not to in to check if a key is not in a dictionary:
"""

# using the same dictionary as the one above instead of repeating the same code

# print("Bill Doors" not in bill)

"""
You can delete a key-value pair from a dictionary with the keyword del:
"""

# books = {"Dracula": "Stoker",
#          "1984": "Orwell",
#          "The Trial": "Kafka"}
#
# del books["The Trial"]
#
# print(books)

"""
Here is an example of a program using a dictionary:
"""

rhymes = {"1": "fun",
          "2": "blue",
          "3": "me",
          "4": "floor",
          "5": "live"
          }

n = input("Type a number:")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Not found. Try again.")