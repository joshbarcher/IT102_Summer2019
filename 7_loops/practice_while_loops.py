# ask the user for numbers and print their sum
# until the sum exceeds 42

sum = 0
while not sum > 42:
    number = input("Enter a number: ")

    if number.isnumeric():
        sum += int(number)
        print("Sum:", sum)
    else:
        print("Please enter a valid integer")

# a word inspector for string length
userInput = ""
while userInput != "stop":
    word = input("Enter a favorite word: ")
    print(word, "has", len(word), "characters")

    # ask the user whether they want to stop
    userInput = input("Enter \"stop\" to stop or enter to continue")
print("Thanks for playing")