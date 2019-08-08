import os

def printFilesIn(dir):
    # make sure the directory is present
    if not os.path.exists(dir):
        print("Folder not found:", dir)
        exit()

    # print out directory contents
    contents = os.listdir(dir)
    for content in contents:
        if os.path.isdir(dir + content):
            print("Directory:", content)
        elif os.path.isfile(dir + content):
            print("File:", content)
        else:
            print(content)
    print()

printFilesIn(".") # current directory
printFilesIn("..") # parent directory
printFilesIn("/documents")