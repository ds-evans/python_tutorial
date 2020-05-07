# An introductory tutorial to python

# String introduction
character_name = "John"
character_age = 35
print("There once was a man, " + character_name + ", who was " + str(character_age));
phrase = "Python Academy"
print(phrase + " is cool")
print(phrase.lower().upper().isupper())
print(phrase[0])
print(phrase[1])
print(phrase.index("A"))
print(phrase.replace("Python", "Snake"))

# Number introduction
number = 5
print("\n" + str(number))
print(3 * (4 + 5))
print(10 % 3)
print(abs(number))
print(pow(number, 2))
print(max(number, 25))
print(round(3.5))

# Importing
from math import *
print(floor(3.9))
print(ceil(3.1))
print(floor(sqrt(25)))

# User Input
input()
