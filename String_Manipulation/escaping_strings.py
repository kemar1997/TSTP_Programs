# If you use quotes inside a string, you will get a syntax error:

# this code does not work just for an example

# print("She said "Surely."")

# You can fix this error by prefacing the quotes with backslashes

print("She said \"Surely.\"")

print('She said \"Surely.\"')

"""
Escaping a string means putting a symbol in front of a character that normally has a special meaning in Python
(in this case, a quote), that lets Python know that, in this instance, the quote is meant to represent a character,
and not the special meaning. Python uses a backslash for escaping.

You do not need to escape single quotes inside of a string with double quotes: 
"""

print("She said 'Surely.'")

"""
You can also put double quotes inside of single quotes, which is simpler than escaping the double quotes:
"""

print('She said "Surely."')