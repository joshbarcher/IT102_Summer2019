
# global list of wardrobe items
items = []

def track(item):
    items.append(item)

def printItems():
    # is the list empty
    if len(items) == 0:
        print("Wardrobe is empty")
    else:
        for item in items:
            print(item)
    print()

def clear():
    items.clear()