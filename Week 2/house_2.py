import turtle



#rectangle = turtle.Turtle()
#rectangle.hideturtle()




def box(start_x, start_y, width, height, fill):
    square = turtle.Turtle()
    #square.hideturtle()
    
    #square.up()
    square.goto(start_x, 101)
    print(start_x)
    print(start_y)
    print(square.xcor())
    print(square.ycor())
    #square.down()
    
    if fill == True:
        square.begin_fill()
        for side in range(2):
            square.forward(width)
            square.right(90)
            square.forward(height)
            square.right(90)
        square.end_fill()
    else:
        for side in range(2):
            square.forward(width)
            square.right(90)
            square.forward(height)
            square.right(90)
        square.end_fill()

        
def triangle():
    triangle = turtle.Turtle()
    triangle.hideturtle()
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
box(-50, 50, 100, 100, False)
#roof
triangle()
#door
box(-10, -10, 20, 40, True)

#left window

#right window
