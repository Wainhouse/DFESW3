# inputNumVar = int(input('Shove a whole number in:'))
# resultVar = 1
# while inputNumVar > 0:

#     resultVar = resultVar * inputNumVar
#     inputNumVar = inputNumVar -1


# print(resultVar)

# for i in range(3):
#     for j in range(4):
#         print(i, "x", j, "=", i * j)

#...is awesome
# count = 0
# name = str(input("What is your name?"))

# while count < 5:
#     print(name, "is awesome!")
#     count += 1

# Print Numbers 5-10
# for i in range(5, 11):
#     print(i)

# for i in range(10, 21, 2):
#     print(i)

# Write a while loop which asks for the names of 5 people, and for each person prints their name followed by the text "is awesome!"

# from typing import Text

# # fail
# count = 0
# name = str(input("What is your name?"))

# list_of_name = [name]

# while count < 5:
#     print(name, "is awesome!")
#     if name == name:

#         name2 = name.replace(input("what is your name?"))
#     print(name2 + "is awesome!")
#     # if name == name:
#     #     str.replace(input("What is your name?"))
#     #     print(name, "is awesome!")

#     count += 1

input = str(input("Insert a word?"))

strlen = len(input)

slicedString = input[strlen::-1]
print(slicedString)

if slicedString == input[strlen::-1]:
    print("You are a palindrome")
