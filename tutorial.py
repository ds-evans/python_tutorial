# # An introductory tutorial to python
#
# # String introduction
# character_name = "John"
# character_age = 35
# print("There once was a man, " + character_name + ", who was " + str(character_age));
# phrase = "Python Academy"
# print(phrase + " is cool")
# print(phrase.lower().upper().isupper())
# print(phrase[0])
# print(phrase[1])
# print(phrase.index("A"))
# print(phrase.replace("Python", "Snake"))
#
# # Number introduction
# number = 5
# print("\n" + str(number))
# print(3 * (4 + 5))
# print(10 % 3)
# print(abs(number))
# print(pow(number, 2))
# print(max(number, 25))
# print(round(3.5))
#
# # Importing
# from math import *
# print(floor(3.9))
# print(ceil(3.1))
# print(floor(sqrt(25)))

# User Input
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "!\nYou are " + age)

# # Building a basic calculator
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
# print(result)

# # Mad libs
# color = input("Enter a color: ")
# plural_noun = input("Enter a Plural Noun: ")
# celebrity = input("Enter a celebrity: ")
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

# # Lists
# friends = ["Tom", "Jim", "Max", "Cynthia", "Karen"]
# print(friends)
# print(friends[0])
# print(friends[-1])
# print(friends[1:])
# print(friends[2:4])

# # List functions
# numbers = [1, 2, 3]
# friends = ["Tom", "Jim", "Max", "Cynthia", "Karen"]
# # friends.extend(numbers)
# friends.append("Creed")
# friends.insert(1, "Kelly")
# friends.remove("Jim")
# # friends.clear()
# friends.pop()
# print(friends.index("Max"))
# print(friends.count("Max"))
# friends.sort()
# friends2 = friends.copy()
# friends2.reverse()
# print(friends2)

# # Tuple introduction
# coordinates = (4, 5)
# # Tuples are immutable
# print(coordinates)

# # Functions
# def say_hi(name, age):
#     print("Hello " + name + " you are " + age)
#
#
# say_hi("Mike", "20")
# say_hi("Steve", "40")

# # Returns
# def cube(num):
#     return num * num * num
#
# resolve = cube(4)
# print(resolve)

# # If statements
# is_male = True
# is_tall = False
# if is_male and is_tall:
#     print("male and tall")
# elif is_male or is_tall:
#     print("male or tall")
# else:
#     print("female and not tall")

# # Comparison operator
# def max_number(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         print(num1)
#     elif num2 >= 1 and num2 >= num3:
#         print(num2)
#     else:
#         print(num3)
#
# max_number(3, 20, 100)

# # Dictionaries
# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March"
# }
# # All keys must be unique
# print(monthConversions["Jan"])
# print(monthConversions.get("Fe"))
# print(monthConversions.get("Fe", "Not valid key"))
#
# # While loops
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# # Guessing game
# word = "stop"
# guess = ""
# times = 0
# limit = 3
# while guess != word and times < limit:
#     guess = input("Enter guess:")
#     times += 1

# For loop
friends = ["Jim", "Karen", "Kevin"]
# for friend in friends:
#     print(friend)
#
# for index in range(10):
#     print(index)
#
# for index in range(len(friends)):
#     print(index)

# Exponent function
# print(2**2)
#
#
# def raise_to(base, power):
#     result = 1
#     for index in range(power):
#         result = result * base
#     return result
#
#
# print(raise_to(3, 3))

# 2D lists and nested loops
# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
#
# print(number_grid[2][1])
#
# for row in number_grid:
#     for column in row:
#         print(column)

# Comments introduction
# Single-line comment
'''
    This is a block comment
'''
# Should only use hashes


