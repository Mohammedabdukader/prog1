import turtle
isak = turtle.Turtle()
turtle.bgcolor ("black")
isak.pensize(2)
isak.speed(0)
for i in range (6):
    for colours in ("red","magenta", "blue", "green", "yellow", "white"):
        isak.color (colours)
        isak.circle (100)
        isak.left (10)
        isak.hideturtle()
turtle.done()