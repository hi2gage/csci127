import turtle

def bobcat_line(drawing_turtle, number_segments, segment_length):
    for i in range(number_segments):
        if i % 2 ==0:
            drawing_turtle.color("blue")
        else:
            drawing_turtle.color("gold")
        drawing_turtle.forward(segment_length)

drawing_turtle = turtle.Turtle()
drawing_turtle.width(3)
drawing_turtle.hideturtle()

number_segments = int(input("Enter number of segments: "))
segment_length = int(input("Enter length of a segment: "))

# Assume the user will enter an integer >= 1 # Assume the user will enter an integer >= 10
bobcat_line(drawing_turtle, number_segments, segment_length)
