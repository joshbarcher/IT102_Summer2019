# bring the turtle module into our script
import turtle

# create a turtle and screen object
pen = turtle.Turtle()
window = turtle.Screen()

# draw the front of the cube
pen.fillcolor("#badebf")
pen.begin_fill()

pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.end_fill()

# draw the top of the cube
pen.fillcolor("#fc9621")
pen.begin_fill()

pen.right(45)
pen.forward(100)
pen.right(45)
pen.forward(100)
pen.right(135)
pen.forward(100)
pen.end_fill()

# draw the side of the cube
pen.fillcolor("#95a4c7")
pen.begin_fill()

pen.left(45)
pen.forward(100)
pen.left(135)
pen.forward(100)
pen.left(45)
pen.forward(100)
pen.left(135)
pen.forward(100)
pen.end_fill()

window.exitonclick()