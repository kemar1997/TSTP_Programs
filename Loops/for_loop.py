"""
loop: a piece of code that continually executes instructions until a condition defined in the code is satisfied
"""

"""
for-loop: a loop used to iterate through an iterable. This process is called iterating. You can use a for-loop to
define instructions that execute once for every item in an iterable, and you can access and manipulate each item
in the iterable from within the instructions you defined. For example, you could use a for-loop to iterate through
a list of strings, and use the upper method to print each string with all of its characters capitalized.

You can define a for-loop using the syntax 'for [variable_name] in [iterable_name]: [instructions]' where 
[variable_name] is a variable name of your choosing assigned to the value of each item in the iterable, and
[instructions] is the code to be executed each time through the loop. Here is an example using a for-loop to iterate
through the characters of a string:
"""

name = "Ted"
for character in name:
    print(character)

"""
Each time around the loop, the variable character gets assigned to an item in the iterable name. The first time around
the loop, T prints because the variable character is assigned to the value of the first item in the iterable name. The
second time around the loop, e prints because the variable character is assigned to the value of the second item in the
iterable name. This process continues until every item in the iterable has been assigned to the variable character.

Here is an example using a for-loop to iterate through the items in a list:
"""
print("\n")
shows = ["GOT",
         "Narcos",
         "Vice"]
for show in shows:
    print(show)

# An example using a for-loop to iterate through items in a tuple:
print("\n")
coms = ("A. Development",
        "Friends",
        "Always Sunny")
for show in coms:
    print(show)

# An example using a for-loop to iterate through the keys in a dictionary:
print("\n")
people = {"G. Bluth II":
          "A. Development",
          "Barney":
          "HIMYM",
          "Dennis":
          "Always Sunny"}

for character in people:
    print(character)

# You can use for-loops to change the items in a mutable iterable, like a list:
print("\n")
tv = ["GOT",
      "Narcos",
      "Vice"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1


print(tv)

"""
In this example, you used a for-loop to iterate the list tv. You keep track of the current item in the list using an
index variable: a variable that holds an integer representing an index in an iterable. The index variable i starts at
0, and is incremented each time around the loop. You can use the index variable to get the current item from the list,
which you then store in the variable new. Next you call the upper method on new, save the result, and use your index
variable to replace the current item in the list with it. Finally, you increment i so you can look up the next item in
the list the next time around the loop.

Because accessing each item and its index in an iterable is so common, Python has another syntax you can use for this:
"""
print("\n")

# Using the same tv list as the previous example

for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new


print(tv)

"""
Instead of iterating through tv, you passed tv to enumerate and iterated through the result, which allowed you to add a
new variable i that keeps track of the current index.

You can use for-loops to move data between mutable iterables. For example, you can use two for-loops to take all the
strings from two different lists, capitalize each character in them, and put them into a new list:
"""

print("\n")

tv = ["GOT", "Narcos",
      "Vice"]
coms = ["Arrested Development",
        "friends",
        "Always Sunny"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)


for show in coms:
    show = show.upper()
    all_shows.append(show)


print(all_shows)