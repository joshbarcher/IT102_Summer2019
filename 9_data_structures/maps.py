# store a look-up table from movie
# to movie genre

genres = {
    "The Wind Rises": "Anime",
    "Rising Sun": "Investigation",
    "IT": "Horror",
    "No Country For Old Men": "Suspense",
    "Akira": "Anime"
}

# print out the keys
for movie in genres:
    print("Movie:", movie)
print()

# print out values
for movie in genres:
    genre = genres[movie]
    print("Genre:", genre)
print()

# you can add more pairs to the map
genres.update({"Matrix": "Sci-fi"})

# print out keys & values together
for movie in genres:
    print("Movie:", movie, ", Genre:", genres[movie])
print()








