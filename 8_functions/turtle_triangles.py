import turtle

pen = turtle.Turtle()
window = turtle.Screen()

# define a function that creates a triangle
def triangle():
    for i in range(3):
        pen.forward(30)
        pen.right(120)

for i in range(7):
    triangle()

    # more the pen
    pen.up()
    pen.right(45)
    pen.forward(40)
    pen.down()

window.exitonclick()