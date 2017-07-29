"""
If you want to read the file, you pass in "r" as the second parameter (mode) to open. Then you call the read method on
your file object, which returns an iterable containing each line of the file:
"""

with open("st.txt", "r") as f:
    print(f.read())

"""
You can only call read on a file once, without closing and reopening it to get its contents, so you should save the file
contents in a variable or container if you need to us them later in your program. Here is how to save the contents from
the file in the previous example in a list:
"""

my_list = list()


with open("st.txt", "r") as f:
    my_list.append(f.read())


print(my_list)


# Now you can access this data later in your program
