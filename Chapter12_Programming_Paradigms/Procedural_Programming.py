"""
In Part I, you programmed using the 'procedural programming' paradigm: a programming style in which you write a sequence
of steps moving toward a solution; with each step changing the program's state. In procedural programming, you write
code to "do this, then that":
"""

x = 2
y = 4
z = 8
xyz = x + y + z
print(xyz)

"""
Each line of code in this example changes the program's state. First, you define x, then y, then z. Finally, you define
the value of xyz.

When you program procedurally, you store data in global variables and manipulate it with functions:
"""

rock = []
country = []


def collect_songs():
    song = 'Enter a song.'
    ask = "Type r or c. q to quit"

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "r":
            rk = input(song)
            rock.append(rk)

        elif genre == "c":
            cy = input(song)
            country.append(cy)

        else:
            print("Invalid.")
    print(rock)
    print(country)

collect_songs()

"""
Procedural programming is fine when building small programs like this, however, because you store all of your program's
state in global variables, you run into problems when your program becomes larger. The problem with relying on global
variables is that they cause unexpected errors. When your program becomes large, you start using global variables in 
multiple functions throughout your program, and it becomes impossible to keep track of all the places a global variable
is modified. For example, a function might change the value of a global variable, and later in the program, a second
might change the same global variable, because the programmer who wrote the second function forgot the first function
already modified it. This situation frequently occurs and corrupts a program's data.

As your program grows in complexity, the number of global variables in it increases. When you combine this increase with
the growth in the number of functions your program needs to handle new functionality, which all modify the global
variables, your program quickly becomes impossible to maintain. Furthermore, this approach to programming relies on side
effects. A side effect is changing the state of a global variable. When you program procedurally, you will often run
into unintended side effects such as accidentally incrementing a variable twice.

This problem led to the development of the object-oriented and functional programming paradigms, and they both take
different approaches to address it.
"""
