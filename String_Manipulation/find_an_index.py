"""
You can get the index of the first occurrence of a character in a string with the index method. Pass in the character
you are looking for as a parameter, and the index method returns the index of the first occurrence of that character
in the string:
"""


print("animals".index("m"))

# Python raises an exception if the index method does not find a match:

# print("animals".index("z"))

# If you are not sure if you will find a match, you can use exception handling:

try:
    print("animals".index("z"))
except ValueError:
    print("Not found.")