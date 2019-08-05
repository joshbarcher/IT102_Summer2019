# read an input string from the user
sentence = input("Enter a (long) sentence: ")

# count up the number of times each
# character shows up in the string
charCounts = {}
for char in sentence:
    # ask if the character is already in the map
    if char in charCounts:
        charCounts[char] += 1
    else:
        charCounts[char] = 1

# print the frequencies
for char in charCounts:
    print(char + ":", charCounts[char])
