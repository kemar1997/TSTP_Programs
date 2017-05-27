"""
You can combine loops in various ways. For example, you can have one loop inside of a loop or a loop inside a loop
inside a loop. There is no limit to the number of loops you can have inside of other loops, although you want to limit
this. When a loop is inside another loop, the second loop is nested in the first loop. In this situation, the loop with
another loop inside it is called an outer loop, and the nested loop is called the inner loop. When you have a nested
loop, the inner loop iterates through its iterable once for each time around the outer loop:
"""

for i in range(1, 4):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)

'''
The nested for-loop will iterate through the list ["a", "b", "c"] however many times the outer loop runs - in this case
, three times. If you changed your outer loop to run four times, the inner loop would iterate through its list four
times as well.

You can use two for-loops to add each number in a list to all the numbers in another list:
'''

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)

print(added)

'''
The first loop iterates through every integer in list1. For each item in it, the second loop iterates through each
integer in its own iterable, adds it to the integer from list1 and appends the result to the list added. I named the
variable j in the second for-loop, because I already used the variable name i in the first loop.

You can nest a for-loop inside a while-loop, and vice versa:
'''

while input("y or n?") != "n":
    for i in range(1, 6):
        print(i)

# This program will print the numbers 1-5 until the user enters n.
