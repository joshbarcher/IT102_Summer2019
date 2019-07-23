import random
import time

# print powers of 10
number = 1
while number <= 1000000: # til 1 million
    print(number)
    number *= 10
print()

# same thing with a for loop
number = 1
for i in range(7):
    print(number)
    number *= 10
print()

# lets print a pattern ////\\\\
pattern = "/\\"
spaces = 9
while len(pattern) <= 20:
    leadingSpace = " " * spaces
    spaces -= 1

    print(leadingSpace + pattern)
    pattern = "/" + pattern + "\\"
print()

# ask the user what lines of a song they
# would like to play
line1 = "She packed my bags last night pre-flight"
line2 = "Zero hour nine AM"
line3 = "And I'm gonna be high as a kite by then"

playingSong = True
while playingSong:
    line = input("Enter line (1-3) or 0 to stop: ")

    if line.isnumeric():
        line = int(line)
        if line == 0:
            playingSong = False
        elif line == 1:
            print(line1)
        elif line == 2:
            print(line2)
        elif line == 3:
            print(line3)
        else:
            print("Please enter 0 to stop or 1-3")
    else:
        print("Please enter a number 0 or 1-3")


# play craps with the user (dice rolling)
continuePlaying = True
while continuePlaying:
    firstDice = random.randint(1, 6)
    secondDice = random.randint(1, 6)

    print("You rolled a", str(firstDice), "and a", str(secondDice))

    # see if they got snake eyes
    if firstDice == 1 and secondDice == 1:
        print("You rolled snake eyes!")

    userChoice = input("Enter 0 to stop")
    if userChoice == "0":
        continuePlaying = False

# flip a coin forever
while True: # infinite loop!
    coin = random.randint(1, 2)

    if coin == 1:
        print("heads")
    else:
        print("tails")

    time.sleep(1) # pause for 1 second