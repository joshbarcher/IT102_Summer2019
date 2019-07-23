
# print a multiplication table
# for i in range(1, 11):
#     for j in range(1, 11):
#         num = i * j
#         print (num, " ", end="")
#
#         # pad single digit numbers with a space
#         if num < 10:
#             print(" ", end="")
#
#     print() # end of row new line
# print()

# get user interests
for i in range(3):
    friend = input("Enter a friend's name: ")
    allInterests = "["

    for j in range(3):
        interest = input("Enter an interest for " + friend + ": ")
        allInterests = allInterests + interest + " "
    allInterests = allInterests + "]"

    print(friend, "is interested in", allInterests)

