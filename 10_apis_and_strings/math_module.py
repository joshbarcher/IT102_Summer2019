import turtle
import math

pen = turtle.Turtle()
window = turtle.Screen()
window.setup(500, 500)

def drawCurve(magnitude, horAdjust, verAdjust):
    pen.up()
    pen.home()
    pen.backward(250)
    pen.down()

    for x in range(360):
        # y = msin(x + h) + v
        y = magnitude * math.sin(x * horAdjust) + verAdjust

        # adjust my x value and move the pen
        x -= 250
        pen.goto(x, y)

drawCurve(20, 0.1, -50)
drawCurve(30, 0.5, -100)
drawCurve(10, 0.9, 0)

window.exitonclick()