"""
There is a second preferred syntax to open files that prevents you from having to remember to close them. To use this
syntax, you put all of your code that needs access to the file object inside a with-statement: a compound statement with
an action that automatically when Python leaves it.

The syntax for opening a file using a with-statement is with open([file_path]), [mode]) as [variable_name]: [your_code].
[file_path] represents the file path, [mode] represents the mode to open the file in. [variable_name] represents the
name of the variable the file object is assigned to, and [your_code] represents the code that has access to the variable
the file object is assigned to.

When you use this syntax to open a file, it automatically closes after the last suite in [your_code] executes. Here is
an example from the previous section using new syntax to open, write to, and close a file:
"""

with open("st.txt", "w") as f:
    f.write("Hello from Python!" + "\n" + "Hello again")

"""
As long as you are inside the with-statement, you can access the file object - in this case, you named it f. As soon as
Python finishes running all the code in the with-statement, Python closes the file for you.
"""