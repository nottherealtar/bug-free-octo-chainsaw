import turtle

def draw_attractive_design4():
    colors = ["red", "yellow", "green"]
    pen = turtle.Turtle()
    pen.speed(17)
    turtle.bgcolor("black")  
    pen.pensize(2)

    size = 20

    for i in range(300):
        pen.color(colors[i % 3])
        pen.forward(size)
        pen.left(59)
        pen.forward(size)
        pen.left(59)
        pen.forward(size)
        pen.left(59)
        pen.forward(size)
        pen.left(121)
        size += 2  

    pen.hideturtle()


draw_attractive_design4()

turtle.done()