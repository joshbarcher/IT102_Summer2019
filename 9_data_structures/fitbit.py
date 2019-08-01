
# continually ask the user for their daily steps
steps = [] # an empty list to start out with

continueAsking = True
while continueAsking:
    dailySteps = int(input("Enter your steps for this day: "))
    steps.append(dailySteps)

    userInput = input("Continue? (yes/no) ")
    if userInput != "yes":
        continueAsking = False

    # continueAsking = input("Continue? (yes/no) ") == "yes"

# then I'm going to print the average steps
sum = 0
for numSteps in steps:
    sum += numSteps

average = sum / len(steps)

print("Your average steps:", average)