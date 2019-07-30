import math

# a function that prints the distance between two points
def distance(x1, y1, x2, y2):
    diffX = x1 - x2
    diffY = y1 - y2

    # square our differences
    diffX **= 2
    diffY **= 2

    distance = math.sqrt(diffX + diffY)
    print("Distance: ", distance)

# invoke the function
distance(10, 2, 1, 1)
distance(3, 3, 2, 5)

# given a number or items and price, this
# function will calculate an order total

def printOrderTotal(numItems, itemPrice, taxRate):
    subTotal = numItems * itemPrice
    taxesOwed = subTotal * taxRate
    total = subTotal + taxesOwed

    total = round(total, 2)

    print("You owe: $" + str(total))

# buy three surfboards at $59.99
printOrderTotal(3, 59.99, 0.098)

# buy five candles at $5.99
printOrderTotal(5, 5.99, 0.098)
