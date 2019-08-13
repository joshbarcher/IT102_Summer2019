
# print out the pages of each book in our CSV file
with open("files/books.csv", "r") as reader:
    lines = reader.readlines()

    # remove the first line of the file
    del lines[0]

    # print out the books
    for line in lines:
        partsList = line.split(",")

        print("Title:", partsList[0])
        print("Pages:", partsList[2])