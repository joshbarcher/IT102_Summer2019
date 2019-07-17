import random

# print patterns on the console
for i in range(1, 11):
    row = "*" * i
    print(row)

# print out the first five positive odd integers
for i in range(15):
    oddNumber = 2 * i + 1
    print(oddNumber, " ", end="")
print()

times = int(input("How many coin flips? "))
for i in range(times):
    number = random.randint(1, 2)

    if number == 1:
        print("heads")
    else:
        print("tails")


