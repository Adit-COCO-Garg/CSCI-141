import turtle

def draw_l(length):
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)

def transition_back(length):
    turtle.back(length)
    turtle.left(90)
    turtle.back(length)
    turtle.righ(90)

def draw_ziggy_boi(length, depth):
    if depth<=0:
        return
    else:
        draw_l(length)
        draw_ziggy_boi(length/2, depth-1)
        transition_back(length)
        turtle.right(180)
        draw_ziggy_boi(length / 2, depth - 1)
        transition_back(length)
        draw_l(length)
        draw_ziggy_boi(length/2, depth-1)
        transition_back(length)
        turtle.right(90)



