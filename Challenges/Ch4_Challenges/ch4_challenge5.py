"""
Write a function that converts a string to a float and returns the result. Use the
exception handling to catch the exception that could occur.
"""


def str_to_float(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert a string to a float")

c = str_to_float("55.0")
print(c)