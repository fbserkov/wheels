from turtle import Turtle


def move(to_angle):
    turtle.setheading(to_angle)
    turtle.forward(50)


turtle = Turtle()
turtle.screen.setup(width=640, height=480)
turtle.penup()
turtle.speed(0)

turtle.screen.onkey(lambda: move(90), 'Up')
turtle.screen.onkey(lambda: move(270), 'Down')
turtle.screen.onkey(lambda: move(180), 'Left')
turtle.screen.onkey(lambda: move(0), 'Right')
turtle.screen.listen()

turtle.screen.mainloop()
