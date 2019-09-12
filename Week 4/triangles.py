"""
file: triangles.py
language: python3
author: ag9126@rit.edu Adit Garg
description: CSCI 141: hw03. The following code draws triangles recursively
    (sirepinski triangle) using depth defined by user.
"""


# Import modules/dependencies
import turtle


def draw_triangles(size, depth):
    """
    pre-conditions: size should be less than 200, depth is a non negative
        integer. turtle facing 60 degrees to the left from east toward North
    draw_triangles: draws Sirepinski Triangle
    post-conditions: None
    """
    if depth < 1:
        return
    elif depth == 1:
        turtle.down()
        turtle.forward(size / 2)
        turtle.left(120)
        turtle.forward(size / 2)
        turtle.left(120)
        turtle.forward(size / 2)
        turtle.up()
    elif depth > 1:
        turtle.down()
        turtle.forward(size)
        draw_triangles(size/2, depth-1)
        turtle.right(120)
        turtle.forward(size)
        turtle.right(120)
        draw_triangles(size/2, depth-1)
        turtle.forward(size)


def main():
    """
        pre-conditions: turtle imported
        main: prompts user for depth and draws Sirepinski Triangle
        post-conditions: None
    """
    depth = int(input("Enter recursion depth! "))
    turtle.left(60)
    draw_triangles(150, depth)
    turtle.left(60)
    turtle.done()


main()