"""
The join method lets you add new characters between every character in a string:
"""

first_three = "abc"
result = " + ".join(first_three)
print(result)

"""
You can turn a list of strings into a single string by calling the join method on an empty string, and passing in the
list as a parameter:
"""

words = ["The",
         "fox",
         "jumped",
         "over",
         "the",
         "fence",
         "."]
one = "".join(words)
print(one)

"""
You can create a string with each word separated by a space by calling the join method on a string with a space in it:
"""

words = ["The",
         "fox",
         "jumped",
         "over",
         "the",
         "fence",
         "."]
one = " ".join(words)
print(one)