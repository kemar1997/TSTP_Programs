"""
The first step to working with a file is to open it with Python's built-in "open" function. The open function takes two
parameters: a string representing the path to the file to open and a string representing the mode to open the file in.

The path to a file, or file path, represents the location on your computer where a file resides. For example, /Users/bob
/st.txt is the file path to a file called st.txt. Each word separated by a slash is the name of a folder. Together, it
represents the location of a file. If a file path only has the name of the file (with no folders separated by slashes),
Python will look for it in whatever folder you are running your program from. You should not write a file path yourself.
Unix-like operating systems and Windows use a different number of backslashes in their file paths. To avoid problems 
with your program working across different operating systems, you should always create file paths using Python's built-
in 'os' module. The path function in it takes each folder in a file path as a parameter and builds the file path for you
:
"""

import os
mypath = os.path.join("Users",
                      "bob",
                      "st.txt")

print(mypath)

"""
Creating file paths with the path function ensures they will work on any operating system. Working with file paths can
still tricky.

The mode you pass to the open function determines the actions you will be able to perform on the file you open. Here are
a few of the modes you can open a file in:

- "r" opens a file for reading only.

- "w" opens a file  for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new
file for writing.

- "w+" opens a file for reading and writing. Overwrites the file if the file exists. If the file does not exist, creates
 a new file for reading and writing.

The open function returns an object, called a file object, which you can use to read and/or write to your file. When you
use the mode "w", the open function creates a new file, if it doesn't already exist, in the directory your program is
running in.

You can then use the write method on the file object to write to the file, and the close method to close it. If you open
a file using the open method, you must close it with the close method. If you use the open method on multiple files and
forget to close them, it can cause problems in your program. Here is an example of opening a file, writing to it, and
closing it:
"""

st = open("st.txt", "w")
st.write("Hi from Python!")
st.close()

"""
In this example, you use the open function to open the file and save the file object it returns in the variable st. Then
you call the write method on st, which accepts a string as a parameter and writes it to the new file Python created.
Finally, you close your file by calling the close method on the file object.
"""