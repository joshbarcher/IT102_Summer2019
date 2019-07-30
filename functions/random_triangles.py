import turtle
import random

pen = turtle.Turtle()
screen = turtle.Screen()

screen.setup(500, 500)

# speed up the drawing
screen.tracer(0)

# function for drawing a triangle
def drawTriangle(x1, y1, x2, y2, x3, y3):
    # move to the first point
    pen.up()
    pen.goto(x1, y1)
    pen.down()

    #draw all three sides
    pen.goto(x2, y2)
    pen.goto(x3, y3)
    pen.goto(x1, y1)

def drawRandomTriangle(howMany):
    for i in range(howMany + 1):
        x1 = random.randint(-250, 250)
        y1 = random.randint(-250, 250)
        x2 = random.randint(-250, 250)
        y2 = random.randint(-250, 250)
        x3 = random.randint(-250, 250)
        y3 = random.randint(-250, 250)

        # call my other function
        drawTriangle(x1, y1, x2, y2, x3, y3)

drawRandomTriangle(5)

screen.exitonclick()