"""
You can use a continue-statement: a statement with the keyword continue - to stop the current iteration of a loop and
move on to the next iteration of it. Say you want to print all the numbers from 1 to 5, except the number 3. You can
achieve this using a for-loop and a continue-statement:
"""

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

"""
In this loop, when i equals 3, your continue-statement executes, and instead of causing your loop to exit completely
like the break keyword would - the loop persists. The loop moves on to the next iteration, skipping any code that
would have executed. When i equals 3, and Python executes the continue-statement, Python does not print the number 3.

You can achieve the same result using a while-loop and a continue-statement:
"""

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1