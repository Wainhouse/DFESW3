# Write a Python function to find the Max of three numbers.

# def max_of_two(x, y):
#     if x > y:
#         return x
#     return y


# def max_of_three(x, y, z):
#     return max_of_two(x, max_of_two(y, z))


# print(max_of_three(-5, 4, 8))

# Write a Python function to sum all the numbers in a list.

def sum_all(nums):
    total = 0
    for i in nums:
        total += i
        return total


print(sum((4, 6, 399, 4, 3)))
