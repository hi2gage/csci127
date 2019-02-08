import turtle
import random
import time

window = turtle.Screen()

square = turtle.Turtle()
square.speed(0)
square.hideturtle()

square.up()
square.goto(-200, 200)
square.down()


for i in range(4):
    square.forward(50)
    square.right(90)

square.up()
square.goto(-205, 205)
square.write("Change Color")

pencil = turtle.Turtle()
pencil.shape("circle")


def drawing_controls(x, y):
    if (-200 <= x <= -150) and (150 <= y <= 200):
        pencil.color(random.random(), random.random(), random.random())

window.onclick(drawing_controls)



pencil.ondrag(pencil.goto)
