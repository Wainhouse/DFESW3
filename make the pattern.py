# 4. Write a Python program to construct the following pattern, using a nested for loop.

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

digit = 5


for i in range(digit):
    for x in range(i):
        print('* ', end="")
    print('')

for i in range(digit, 0, -1):
    for x in range(i):
        print('* ', end="")
    print('')
