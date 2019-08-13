
# read the file speech.txt and print it out
with open("files/speech.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        print(line, end="")
print()

# read a file line-by-line
with open("files/baby_names.txt") as file:
    # read the first 20 lines of the file
    for i in range(20):
        print(file.readline(), end="")
print()
