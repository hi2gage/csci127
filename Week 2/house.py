import turtle

square = turtle.Turtle()
square.hideturtle()

rectangle = turtle.Turtle()
rectangle.hideturtle()

triangle = turtle.Turtle()
triangle.hideturtle()

#house outline
square.up()
square.goto(-50, 50)
square.down()
for side in range(4):
    square.forward(100)
    square.right(90)

#roof
triangle.up()
triangle.color("red")
triangle.goto(-50, 50)
triangle.down()
triangle.begin_fill()
triangle.goto(0, 100)
triangle.goto(50, 50)
triangle.goto(-50, 50)
triangle.end_fill()

#door
rectangle.up()
rectangle.goto(-10, -10)
rectangle.down()
rectangle.begin_fill()
for half in range(2):
    rectangle.forward(20)
    rectangle.right(90)
    rectangle.forward(40)
    rectangle.right(90)
rectangle.end_fill()

#left window
square.up()
square.goto(-30, 30)
square.down()
for side in range(4):
    square.forward(20)
    square.right(90)

#right window
square.up()
square.goto(10, 30)
square.down()
for side in range(4):
    square.forward(20)
    square.right(90)
