# This file contains some practice statements for io on
# the python console.
# Author: Josh Archer
# Date: 7/1/2019
# File: calculator.py

# get some numbers for arithmetic
first = input("Enter an operand: ")
second = input("Enter an operand: ")

# convert the string inputs to integers
first = int(first)
second = int(second)

# perform some calculations
mult = first * second
div = first / second
add = first + second
sub = first - second

# print the results of the calculation
print("Multiplied: ", str(mult))
print("Divided: ", str(div))
print("Added: ", str(add))
print("Subtracted: ", str(sub))