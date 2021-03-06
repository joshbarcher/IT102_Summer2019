import turtle

# get a pen and move it to the starting position
pen = turtle.Turtle()
pen.speed(0)

window = turtle.Screen()
window.setup(1000, 400)

pen.up()
pen.left(180)
pen.forward(300)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.down()

# draw the s
pen.fillcolor("yellow")
pen.begin_fill()

pen.forward(100)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(80)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(80)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(80)
pen.left(90)
pen.forward(60)
pen.left(90)
pen.forward(80)
pen.right(90)
pen.forward(90)
pen.end_fill()

# draw the a
pen.up()
pen.right(90)
pen.forward(150)
pen.down()

pen.fillcolor("pink")
pen.begin_fill()

pen.forward(100)
pen.right(90)
pen.forward(170)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(70)
pen.left(90)
pen.forward(60)
pen.left(90)
pen.forward(70)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(170)
pen.end_fill()

pen.up()
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(20)
pen.left(90)
pen.down()

pen.fillcolor("white")
pen.begin_fill()

pen.forward(60)
pen.right(90)
pen.forward(60)
pen.right(90)
pen.forward(60)
pen.right(90)
pen.forward(60)
pen.end_fill()

# draw the r
pen.up()
pen.forward(20)
pen.right(90)
pen.forward(130)
pen.down()

pen.fillcolor("blue")
pen.begin_fill()

pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(60)
pen.left(130)
pen.forward(90)
pen.right(130)
pen.forward(20)
pen.right(50)
pen.forward(90)
pen.left(140)
pen.forward(70)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(170)
pen.end_fill()

pen.up()
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(20)
pen.left(90)
pen.down()

pen.fillcolor("white")
pen.begin_fill()

pen.forward(60)
pen.right(90)
pen.forward(60)
pen.right(90)
pen.forward(60)
pen.right(90)
pen.forward(60)
pen.end_fill()

# draw the a
pen.up()
pen.forward(20)
pen.right(90)
pen.forward(130)
pen.down()

pen.fillcolor("pink")
pen.begin_fill()

pen.forward(100)
pen.right(90)
pen.forward(170)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(70)
pen.left(90)
pen.forward(60)
pen.left(90)
pen.forward(70)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(170)
pen.end_fill()

pen.up()
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(20)
pen.left(90)
pen.down()

pen.fillcolor("white")
pen.begin_fill()

pen.forward(60)
pen.right(90)
pen.forward(60)
pen.right(90)
pen.forward(60)
pen.right(90)
pen.forward(60)
pen.end_fill()

# draw the h
pen.up()
pen.forward(20)
pen.right(90)
pen.forward(130)
pen.down()

pen.fillcolor("green")
pen.begin_fill()

pen.forward(20)
pen.right(90)
pen.forward(80)
pen.left(90)
pen.forward(80)
pen.left(90)
pen.forward(80)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(170)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(80)
pen.left(90)
pen.forward(80)
pen.left(90)
pen.forward(80)
pen.right(90)
pen.forward(20)
pen.right(90)
pen.forward(170)

pen.end_fill()

window.exitonclick()