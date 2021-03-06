# The built-in modules used as an example in this part of the chapter

import math
import random
import statistics
import keyword

"""
To use a module, you must first import it: which means writing code, so Python knows where to look for it. You can
import a module with the syntax import [module_name]. Replace [module_name] with the name of the module you are import-
ing. Once you've imported a module, you can use variables and functions from it.

Python has many different modules, including a math module containing math-related functionality. You can find a list of
all of Python's built-in modules at https://docs.python.org/3/py-modindex.html. Here is how to import Python's math
module:
"""

# import math

"""
Once you have imported a module, you can use code from it with the syntax [module_name].[code], replacing [module_name]
with the name of a module you already imported, and [code] with the name of the function or variable you want to use
from it. The following is an example of importing and using the pow function from the math module, which takes two
params, x and y, and raises x by y:
"""

print(math.pow(2, 3),
      math.pow(3, 3),
      math.pow(4, 3),
      math.pow(5, 3))

"""
The random module is another built-in module. You can use a function from it called 'randint' to generate a random
integer: you pass two integers, and it returns a random integer between them:
"""

print(random.randint(0, 100))

"""
You can use the built-in 'statistics' module to calculate the mean, median, and mode in an iterable of numbers:
"""

# mean
nums = [1, 5, 33, 12, 46, 33, 2]
print(statistics.mean(nums))

# median
print(statistics.median(nums))

# mode
print(statistics.mode(nums))

'''
Use the built-in "keyword" module to check if a string is a Python keyword:
'''

print(keyword.iskeyword("for"))
print(keyword.iskeyword("football"))
