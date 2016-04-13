import turtle


def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_triangle(some_turtle):
    for i in range(1, 3):
        some_turtle.forward(100)
        some_turtle.right(120)


def draw_stem(some_turtle):
    some_turtle.forward(50)
    some_turtle.right(90)
    some_turtle.forward(150)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("darkgreen")

    turtle1 = turtle.Turtle()
    turtle1.shape("turtle")
    turtle1.color("yellow")
    turtle1.speed(10)

    for i in range(1, 37):
        draw_triangle(turtle1)
        turtle1.right(10)

    draw_stem(turtle1)
    window.exitonclick()

draw_art()
