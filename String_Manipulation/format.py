"""
You can create a new string using the format method, which looks for occurrences of curly brackets {} in the string,
and replaces them with the parameters you pass in:
"""

print("William {}".format("Faulkner"))

# You can also pass a variable as a parameter

last = "Faulkner"
print("William {}".format(last))

# You are not limited to using curly brackets once, you can use them in your string as often as you would like:

author = "William Faulkner"
year_born = "1897"

print("{} was born in {}.".format(author, year_born))

# The format method is useful if you are creating a string from user input:

n1 = input("Enter a noun:")
v = input("Enter a verb:")
adj = input("Enter a adj:")
n2 = input("Enter a noun:")

r = """The {} {} the {} {}
    """.format(n1,
               v,
               adj,
               n2)

print(r)