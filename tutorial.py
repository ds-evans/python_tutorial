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

