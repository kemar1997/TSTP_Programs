"""
Strings, like lists and tuples, are iterable. You can look up each character in a string with an index. Like other
iterables, the first character in a string is at index 0, and each subsequent index is incremented by 1:
"""

# author = "Kafka"
# print(author[0])
# print(author[1])
# print(author[2])
# print(author[3])
# print(author[4])

"""
In this example, you used the indexes 0, 1, 2, 3, and 4 to look up each of the characters in the string "Kafka".
If you try to look up a character past the last index in you string, Python raises an exception:
"""

# author = "Kafka"
# print(author[5])
# >>> IndexError: string index out of range

"""
Python also allows you to look up each item in a list with a negative index: an index (that must be a negative number)
you can use to look up items in an iterable from right to left, instead of left to right. You can use the negative
index -1 to look up the last item in an iterable:
"""

author = "Kafka"
print(author[-1])

"""
The negative index -2 looks up the second to last item, the negative index -3 looks up the item third to last, and
so on:
"""

# Continue from last example

print(author[-2])
print(author[-3])
print(author[-4])
print(author[-5])