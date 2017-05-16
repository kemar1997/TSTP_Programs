"""
Lists are represented with brackets. There are two syntaxes you can use to create a list.
You can create an empty list with the 'list' function:
"""

# fruit = list()
# fruit

'''
Or, with brackets:
'''

# fruit = []
# print(fruit)

"""
You can create a list with items already in it by using the second syntax [], and
placing each item you want in the list inside the brackets, separated by commas:
"""

# fruit = ["Apple", "Orange", "Pear"]
# print(fruit)

"""
Add a new item to a list using the append method:
"""

# fruit = ["Apple", "Orange", "Pear"]
# fruit.append("Banana")
# fruit.append("Peach")
# print(fruit)

"""
Each object passed to the append method is now an item in your list. append always
adds a new item to the end of the list

Lists are not limited to storing things, they can store an data type:
"""

# random = []
# random.append(True)
# random.append(100)
# random.append(1.1)
# random.append("Hello")
# print(random)

"""
You can retrieve an item with its index using the syntax [list_name][[index]]:
"""

# fruit = ["Apple", "Orange", "Pear"]
# print(fruit[0])
# print(fruit[1])
# print(fruit[2])

"""
If you try to access an index that doesn't exist, Python raises an exception:
"""

# colors = ["blue", "green", "yellow"]
# print(colors[4])

"""
Lists are mutable. When a container is mutable, you can add or remove objects from the
container. You can change an item in a list by assigning its index to a new object:
"""

# colors = ["blue", "green", "yellow"]
# print(colors)
# colors[2] = "red"
# print(colors)

"""
You can remove the last item from a list using the method pop:
"""

# colors = ["blue", "green", "yellow"]
# print(colors)
# item = colors.pop()
# print(item)
# print(colors)

"""
You cannot use pop on an empty list. If you try to, Python will raise an exception.

You can combine two lists with the addition operator:
"""

# colors1 = ["blue", "green", "yellow"]
# colors2 = ["orange", "pink", "black"]
# print(colors1 + colors2)

"""
You can check if a item is in a list with the keyword in:
"""

# colors = ["blue", "green", "yellow"]
# print("green" in colors)

"""
Use the keyword not to check if an item is not in a list:
"""

# colors = ["blue", "green", "yellow"]
# print("black" not in colors)

"""
You can get the size of a list (the number of items in it) with the len function:
"""

# print(len(colors))

"""
Here is an example of how you might use a list in practice:
"""

colors = ["purple",
          "orange",
          "green"]

guess = input("Guess a color:")

if guess in colors:
    print("You guessed correctly!")
else:
    print("Wrong! Try again.")

"""
The colors list contains different strings representing colors. The program uses the
built-in "input" function to ask the user to guess a color, and you save their answer
in a variable. If their answer is in the colors list, the program lets the user know
they guessed correctly. Otherwise, it prompts them to guess again.
"""