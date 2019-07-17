# read in user inputs (an RGB color)
red = int(input("Red component? "))
green = int(input("Green component? "))
blue = int(input("Blue component? "))

# check if gray-scale
if red == green and green == blue:
    # just check the red component since all values are equal
    if red == 0:
        print("This color is black")
    elif red == 255:
        print("This color is white")
    else:
        print("This is a gray-scale color")
else:
    # if not print the color components
    print("This is not a gray-scale color")
    print("Color: (" + str(red) + "," + str(green) + ","
          + str(blue) + ")")

    if red != 0:
        print("This color has red in it")

    if green != 0:
        print("This color has green in it")

    if blue != 0:
        print("This color has blue in it")
