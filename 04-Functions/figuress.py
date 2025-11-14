import turtle

def draw_square(length):
    
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    # Side length
    side_length = length

    # Draw a square
    for i in range(4):
        pen.forward(side_length)
        pen.right(90)

    # Hide the turtle and finish
    pen.hideturtle()
    window.mainloop()


draw_square(100)