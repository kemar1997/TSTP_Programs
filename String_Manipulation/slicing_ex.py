"""
Slicing is a way to return a new iterable from a subset of the items in another iterable. The syntax for slicing is
[iterable][[start_index:end_index]]. The start index is the index to start slicing from, and the end index is the index
to stop slicing at.
"""

# Here is how to slice a list:

fict = [
    "Tolstoy",
    "Camus",
    "Orwell",
    "Huxley",
    "Austin"
]

print(fict[0:3])

"""
With slicing, the start index includes the item at that index, but the end index only includes the item before the end
index. Because of this, if you want to slice from "Tolstoy" (index 0) to "Orwell" (index 2), you need to slice from 
index 0 to index 3.
"""

# Here is an example of slicing a string:

ivan = """In place of death there was light."""

print(ivan[0:17])
print(ivan[17:33])

# If your start index is 0, you can leave the start index empty:

print(ivan[:17])

"""
If your end index is the index of the last item in the iterable, you can leave the end index empty:
"""

print(ivan[17:])

# Leaving both the start and end index empty it returns the original iterable:

print(ivan[:])