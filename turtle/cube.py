# bring the turtle module into our script
from turtle import *

# create a turtle object (a pen to draw with)
pen = Turtle()

# draw the front of the cube
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)

# draw the top of the cube
pen.right(45)
pen.forward(100)
pen.right(45)
pen.forward(100)
pen.right(135)
pen.forward(100)

# draw the side of the cube
pen.left(45)
pen.forward(100)
pen.left(135)
pen.forward(100)
pen.left(45)
pen.forward(100)

exitonclick()