
# create a new book in our file
def addBook():
    print("Please enter the following book data: ")

    title = input("Title: ")
    author = input("Author: ")
    pages = input("Pages: ")
    year = input("Year: ")

    with open("files/books.csv", "a") as updater:
        updater.write(title + "," + author + "," + pages +
                      "," + year)

addBook()