"""
1. Writing a function that takes a number as an input and returns that number squared.
"""


def square_a_number():
    num = input("Enter a number: ")
    num = int(num)
    return num*num

result = square_a_number()

print(result)