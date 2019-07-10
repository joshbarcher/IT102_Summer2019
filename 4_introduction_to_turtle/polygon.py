# bring the 4_introduction_to_turtle module into our script
import turtle

# create a 4_introduction_to_turtle and screen object
pen = turtle.Turtle()
window = turtle.Screen()

# draw a six-sided shape
sides = 6
degrees = 360 / sides

pen.color("black")
pen.fillcolor("yellow")

pen.begin_fill()
for i in range(sides) :
    pen.forward(50)
    pen.left(degrees)
pen.end_fill()

#move the pen
pen.up()
pen.goto(-100, -100)
pen.down()

# draw a eight-sided shape
sides = 8
degrees = 360 / sides

pen.color("black")
pen.fillcolor("brown")

pen.begin_fill()
for i in range(sides) :
    pen.forward(50)
    pen.left(degrees)
pen.end_fill()

#move the pen
pen.up()
pen.goto(100, 100)
pen.down()

# draw a twenty-sided shape
sides = 20
degrees = 360 / sides

pen.color("black")
pen.fillcolor("red")

pen.begin_fill()
for i in range(sides) :
    pen.forward(50)
    pen.left(degrees)
pen.end_fill()

#move the pen
pen.up()
pen.goto(100, -100)
pen.down()

# draw a three-sided shape
sides = 3
degrees = 360 / sides

pen.color("black")
pen.fillcolor("purple")

pen.begin_fill()
for i in range(sides) :
    pen.forward(50)
    pen.left(degrees)
pen.end_fill()

window.exitonclick()