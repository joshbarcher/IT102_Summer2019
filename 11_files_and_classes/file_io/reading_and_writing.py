
# read all lines of the file
with open("files/song.txt", "r") as reader:
    lines = reader.readlines()

# remove repetitive lines
changes = []
for line in lines:
    if not "[4x]" in line:
        changes.append(line)

# write the results to a new file
with open("files/song_abbrev.txt", "w") as writer:
    for line in changes:
        writer.write(line)