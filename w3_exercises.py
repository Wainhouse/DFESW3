# 1) Write a Python function to find the Max of three numbers.

# def max_of_two(x, y):
#     if x > y:
#         return x
#     return y


# def max_of_three(x, y, z):
#     return max_of_two(x, max_of_two(y, z))


# print(max_of_three(-5, 4, 8))

# 2)Write a Python function to sum all the numbers in a list.

# def sum_all(nums):
#     total = 0
#     for i in nums:
#         total += i
#         return total


# print(sum((4, 6, 399, 4, 3)))

# 3) Write a Python function to multiply all the numbers in a list.

# def multi_all(nums):
#     total = 1
#     for i in nums:
#         total *= i
#     return total


# print(multi_all((2, 3)))

# 4) Write a Python program to reverse a string.

# ample String : "1234abcd"

# def reverse(string):
#     for i in string:
#         return string[::-1]


# print(reverse("Luke"))

# 5 Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.


# 6 Write a Python function to check whether a number falls in a given range.

# def rang(num, x, y):
#     if num in range(x, y):
#         return("yes")
#     else:
#         return("no")


# print(rang(200, 0, 100))

# 7 Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def count_up(word):
    countUp = 0
    for i in word:
        if i.isupper():
            countUp += 1
    return countUp


def count_low(word):
    countLow = 0
    for i in word:
        if i.islower():
            countLow += 1
    return countLow


countUp = count_up("I am A BanANa")
countLow = count_low("I am A BanANa")

print(countLow)
