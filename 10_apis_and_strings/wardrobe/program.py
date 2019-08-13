# import my module
import wardrobe

# add a few elements, print them
print("Adding a few elements to the wardrobe...")
wardrobe.track("white/brown shirt")
wardrobe.track("khaki shorts")
wardrobe.track("neon socks")
wardrobe.printItems()

# remove all elements, print them
print("Removing elements in the wardrobe...")
wardrobe.clear()
wardrobe.printItems()


# add a few elements, print them
wardrobe.track("khaki shorts")
wardrobe.track("neon socks")
wardrobe.printItems()