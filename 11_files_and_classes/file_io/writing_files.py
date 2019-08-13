
# write a record of data to a file
with open("files/records.txt", "a") as writer:
    writer.write("*" * 30 + "\n")
    writer.write("Name: Jose Torres\n")
    writer.write("Occupation: Technical Writer\n")
    writer.write("*" * 30 + "\n")
