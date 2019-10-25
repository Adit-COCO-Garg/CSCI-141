"""
file: zigzag.py
language: python3
author: ag9126@rit.edu Adit Garg
description: CSCI 141: lab03. The following code draws recursive zig-zags
based on user defined depth. The zig zags change color every depth.
"""

# Import modules/dependencies
import turtle


def draw_l(length):
    """
    pre-conditions: length = positive real number > 0
    draw_l: draws an L
    post-conditions:turtle pen is up and ends at the where it ends drawing
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(length / 2)
    turtle.right(90)
    turtle.forward(length)
    turtle.up()


def transition_back(length):
    """
        pre-conditions: Length = positive real number > 0
        transition_back: draws an L but backwards with pen up (transitions back)
        post-conditions: transitions back in a reverse L shape
    """
    turtle.up()
    turtle.back(length)
    turtle.left(90)
    turtle.back(length / 2)
    turtle.right(90)


def draw_zigg(length, depth):
    """
        pre-conditions: length = a positive real number > 0, depth =
        non-negative  integer
        draw_zigg: draws half of the recursive image, this allows further
        code re-usability and colors that zig or zag based upon the depth
        post-conditions: turtle ends facing opposite to where it started and
        turtle.up
    """
    if depth % 2 == 0:
        turtle.color("#d90d58")
    else:
        turtle.color("#fcba03")
    draw_l(length)
    turtle.left(45)  # tilting
    draw_ziggy_boi(length / 2, depth - 1)
    turtle.right(45)  # de-tilting
    transition_back(length)
    turtle.right(180)


def draw_ziggy_boi(length, depth):
    """
        pre-conditions: length= a positive real number > 0,depth = non-negative
            integer
        draw_zigg: draws the recursive zig-zags with varying color at
        different depths
        post-conditions: turtle ends where it started
    """
    if depth <= 0:
        return 0
    else:
        draw_zigg(length, depth)  # draw zig * depth
        draw_zigg(length, depth)  # draw zag * depth


def main():
    """
        pre-conditions: Turtle is imported and depth is a non-negative integer
        main: draws the recursive zig-zags based upon the depth provided by
            the user
        post-conditions: turtle ends where it started with pen up and the image
            drawn
    """
    # turtle.tracer(False)  # turn this on or off for faster turtle drawings
    # turtle.width(2)  # turn this on or off for better visibility when depth
    # is small
    depth = int(input("Enter the the depth for the drawing! \nDepth: "))
    draw_ziggy_boi(100, depth)
    turtle.done()


main()
