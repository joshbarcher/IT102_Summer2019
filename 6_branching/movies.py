# movie suggestions!
genre = input("What's your favorite movie genre? ")
genre = genre.lower()

# hold two movie suggestions in these variables
firstMovie = "The Fellowship of the Ring"
secondMovie = "The Silence of the Lambs"

print("Searching for a movie suggestion.")
if genre == "capers":
    firstMovie = "Ocean's Eleven"
    secondMovie = "The Italian Job"

elif genre == "romance":
    firstMovie = "10 Things I Hate About You"
    secondMovie = "Cinderella"

elif genre == "horror":
    firstMovie = "Cabin in the Woods"
    secondMovie = "It"

else:
    print("I don't know this genre.",
          "Here are some general suggestions.")

print(firstMovie)
print(secondMovie)