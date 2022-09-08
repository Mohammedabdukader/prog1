import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed (0)
for i in range (6):
    for colours in ( "red", "magenta", "blue", "cyan" ,"yellow", "white"):
        turtle.color(colours)
        turtle.triangel (10)
        turtle.left (10)
turtle.hideturtle()
turtle.done()

