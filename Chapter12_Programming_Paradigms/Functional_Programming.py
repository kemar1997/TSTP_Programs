"""
Functional programming originates from the lambda calculus: the smallest universal programming language
in the world (created by the mathematician Alonzo Church). Functional programming addresses the problems
that arise in procedural programming by eliminating global state. A functional programmer relies on
functions that do not use or change global state, the only state they  use are the parameters you pass
to a function. The result a function returns is usually passed on to another function. A functional
programmer can thus avoid global state by passing it from function to function. Eliminating global
state removes side effects and the problems that come with them.

There is a lot of jargon in functional programming, and Mary Rose Cook cuts through it with her definition,
"Functional code is characterized by one thing: the absence of side  effects. It doesn't rely on data outside
the current function, and it doesn't change data that exists outside the current function." She follows her
definition with an example of a function that has side effects:
"""

a = 0

def increment():
    global a
    a += 1

# And a function with no side effects:

def increment(a):
    return a + 1

"""
The first function has side effects because it relies on data outside of itself, and changes data outside of the
current function; it incremented a global variable. The second function does not have side effects because it
does not rely on or change any data outside of itself.

One advantage of functional programming is that it eliminates an entire catergory of errors caused by global state
(there is no global state in functional programming). A disadvantage of functional programming is certain problems
are easier to conceptualize (form a concept or idea of something) with state. For example, it is simpler to conceptualize
designing a user interface with global state than a user interface without global state. If you want to write a program with
a button that toggles a picture between being shown to the user and being invisible, it is easier to think about how to
create such a button by writing a program with global state. You could create a global variable that is either True or False
that hides or reveals the picture, depending on its current value. It is harder to conceptualize designing a button like this
without global state.
"""
