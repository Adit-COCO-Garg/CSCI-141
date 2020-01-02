import turtle

def triangle_side(side):
    for i in (1,2,3):
        turtle.forward(side)
        turtle.left(120)

turtle.speed(1)
triangle_side(1000)

turtle.done()