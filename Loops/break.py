"""
You can use a break-statement: a statement with the keyword break - to terminate a loop. The following loop will run
one hundred times:
"""

# for i in range(0, 100):
#     print(i)

"""
If you add a break-statement, the loop only runs once:
"""

# for i in range(0, 100):
#     print(i)
#     break

# Separate example

# for i in range(0, 100):
#     print(i)
#     if i is 50:
#         break


"""
You can use a while-loop and the break keyword to write a program that keeps asking the user for input until the type q
to quit
"""

qs = ["What is your name?",
      "What is your fav. color?",
      "What is your quest?"]
n = 0
while True:
        print("Type q to quit")
        a = input(qs[0])
        b = input(qs[1])
        c = input(qs[2])
        if a == "q":
            break
        result = [a, b, c]
        print(result)