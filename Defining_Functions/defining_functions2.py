"""
You can save the result your function returns in a variable whenever you need to use the
value later in your program. Here is an example of that.
"""


def f(x):
    return x + 1

z = f(6)


if z == 5:
    print("z is 5")
else:
    print("z is not 5, z is equal to " + str(z))