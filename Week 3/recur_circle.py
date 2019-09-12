import random
import turtle


def random_color():
    red = random.random()
    green = random.random()
    blue = random.random()
    turtle.pencolor(red, green, blue)


def draw_spiral(length, n):
    random_color()
    if length < 1:
        return 0
    else:
        turtle.left(360/n)
        turtle.forward(length)
        return length + draw_spiral(length-1, n)


def tester():
    turtle.width(3)
    turtle.speed(0)
    print(draw_spiral(50,10))
    turtle.done()

tester()