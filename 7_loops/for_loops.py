
# using sequences with a for-loop
message = "message in a bottle" # string sequences
messageLength = len(message)
print("Message is", str(messageLength), "characters")

for character in message:
    print(character)

# list sequences
for city in ["Tacoma", "Seattle", "Puyallup", "Olympia"]:
    print(city)

# using the range() function to generate lists
for i in range(100):
    print(i)

# loop over the lines in a file
file = open("poem.txt", "r")
lines = file.readlines()

for line in lines:
    print(line, end="")
print()

for i in range(2, -3, -1):
    print(i)