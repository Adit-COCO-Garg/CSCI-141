"""
file: scenery.py
language: python3
author: ag9126@rit.edu Adit Garg
description: CSCI 141: Lab02. The following code
Draws a scenery
"""

# Import modules/dependencies
import turtle, math


def draw_rec_poly(width, height, color):
    """
    pre-conditions:
    quadratic_roots:
    post-conditions: none
    """
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()
    turtle.up()
    return width*height


def draw_house(width, height, angle, color):
    """
    pre-conditions:
    quadratic_roots:
    post-conditions: none
    """
    draw_rec_poly(width, height, color)
    if (height/width) >= 1:
        draw_rec_poly(width, height, "Blue")  # Draw Windows
        draw_rec_poly(width, height, "Blue")  # Draw Windows
        draw_rec_poly(width, height, "Blue")  # Draw Windows
        draw_rec_poly(width, height, "Blue")  # Draw Windows
    else:
        draw_rec_poly(width, height, "Blue")  # Draw Windows
        draw_rec_poly(width, height, "Blue")  # Draw Windows
    draw_roof(width, angle, color)
    draw_rec_poly(width, height, color)  # Draw door


def draw_roof(base, angle, color):
    turn_angle = (180-angle)/2
    isosceles_teri_side = (base/2)/(math.degrees(math.cos(angle)))
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(base)
    turtle.left(turn_angle)
    turtle.forward(isosceles_teri_side)
    turtle.left(angle)
    turtle.forward(isosceles_teri_side)
    turtle.left(turn_angle)
    return 0.5*base*isosceles_teri_side*math.degrees(math.sin(turn_angle))


def canvas_creat(sizeHouse):
    turtle.setup(width=8*sizeHouse, height=4*sizeHouse, startx=0, starty=0)
    turtle.up()
    turtle.setx(-.5*sizeHouse)
    turtle.sety(-1.3*sizeHouse)


def tester():
    canvas_creat(100)



def main():
    """
    pre-conditions: Math library has to be imported!
    main: Calls upon the tester function to test the functionality of the
        program
    post-conditions: none
    """
    tester();
    turtle.done()


main()
# """
# file: scenery.py
# language: python3
# author: ag9126@rit.edu Adit Garg
# description: CSCI 141: Lab02. The following code
# Draws a house based on parameters: size, house
# color, and roof color, and draws a sun relative
# """
# # Import modules/dependencies
# import turtle, datetime
#
# hourRightNow = datetime.datetime.now().hour  # current hour
#
#
# # imported in 24 hours format
#
# def house(sizeHouse, houseColor, roofColor):
#     canvasCreat(sizeHouse)  # Screen-size is based upon the size
#     # of the size of house ensuring elements fit within the screen
#     turtle.up()
#     turtle.left(90)
#     walls(sizeHouse, houseColor)
#     # Transition to next element
#     turtle.forward(sizeHouse * (1 / 4))
#     turtle.right(90)
#     turtle.forward(sizeHouse / 8)
#     turtle.left(90)
#     windows(sizeHouse)
#     # Transition to next element
#     turtle.right(90)
#     turtle.back(sizeHouse / 8)
#     turtle.left(90)
#     turtle.back(sizeHouse * (1 / 4))
#     turtle.right(90)
#     turtle.forward(sizeHouse * (2.5 / 4))
#     turtle.left(90)
#     door(sizeHouse)
#     # Transition to next element
#     turtle.left(90)
#     turtle.forward(sizeHouse * (2.5 / 4))
#     turtle.right(90)
#     turtle.forward(sizeHouse)
#     roof(sizeHouse, roofColor)
#     # Transition to next element
#     turtle.back(sizeHouse)
#     turtle.left(90)
#     turtle.forward(sizeHouse * (13 / 10))
#     turtle.right(90)
#     trees(sizeHouse)
#     # Transition to next element
#     turtle.right(90)
#     turtle.forward((sizeHouse * (26 / 10)) + sizeHouse)
#     turtle.left(90)
#     trees(sizeHouse)
#     # Transition to next element
#     turtle.right(90)
#     turtle.back(sizeHouse * (13 / 10) + sizeHouse)
#     turtle.left(90)
#     if 10 <= hourRightNow <= 14:
#         turtle.forward(sizeHouse * (37 / 10))
#         sun(sizeHouse)
#     elif 10 > hourRightNow:
#         turtle.left(85)
#         turtle.forward(sizeHouse * (37 / 10))
#         sun(sizeHouse)
#     else:
#         turtle.right(85)
#         turtle.forward(sizeHouse * (37 / 10))
#         sun(sizeHouse)
#
#
# def canvasCreat(sizeHouse):
#     # Screen variables and default turtle location defined.
#     turtle.setup(width=8 * sizeHouse, height=4 * sizeHouse, startx=0, starty=0)
#     turtle.up()
#     # turtle.setx(-50)
#     # turtle.sety(-150)
#     turtle.setx(-.5 * sizeHouse)
#     turtle.sety(-1.3 * sizeHouse)
#     # ---
#
#
# def init(sizeHouse):
#     turtle.up()
#     turtle.left(180)
#     turtle.forward(sizeHouse / 2)
#     turtle.right(90)
#
#
# def sun(sizeHouse):
#     turtle.right(90)
#     turtle.down()
#     turtle.color("orange")
#     turtle.begin_fill()
#     turtle.circle(sizeHouse / 3)
#     turtle.end_fill()
#     turtle.up()
#
#
# def trees(sizeHouse):
#     turtle.down()
#     turtle.color("saddle brown")
#     turtle.begin_fill()
#     quadrilateral(sizeHouse, sizeHouse / 10)  # call to quad... function
#     turtle.end_fill()
#     turtle.up()
#     turtle.forward(sizeHouse)
#     turtle.right(90)
#     turtle.forward(sizeHouse / 20)
#     turtle.right(90)
#     turtle.forward(sizeHouse / 20)
#     turtle.left(90)
#     turtle.color("sea green")
#     turtle.begin_fill()
#     turtle.circle(sizeHouse / 4)
#     turtle.end_fill()
#     turtle.up()
#     turtle.back(sizeHouse / 20)
#     turtle.left(90)
#     turtle.back(sizeHouse * (19 / 20))
#
#
# def walls(sizeHouse, houseColor):
#     turtle.down()
#     turtle.color(houseColor)
#     turtle.begin_fill()
#     quadrilateral(sizeHouse, sizeHouse)  # call to quad... function
#     turtle.end_fill()
#     turtle.up()
#
#
# def windows(sizeHouse):
#     turtle.down()
#     turtle.color("CornflowerBlue")
#     turtle.begin_fill()
#     quadrilateral(sizeHouse * (1 / 2),
#                   sizeHouse * (1 / 4))  # call to quad... function
#     turtle.end_fill()
#     turtle.up()
#
#
# def door(sizeHouse):
#     turtle.down()
#     turtle.color("saddle brown")
#     turtle.begin_fill()
#     quadrilateral(sizeHouse * (2 / 3),
#                   sizeHouse / 3)  # call to quad... function
#     turtle.end_fill()
#     turtle.up()
#
#
# def roof(sizeHouse, roofColor):
#     turtle.left(90)
#     turtle.forward(sizeHouse * (1 / 16))
#     turtle.right(90)
#     turtle.down()
#     turtle.color(roofColor)
#     turtle.begin_fill()
#     triangleShape(sizeHouse * (9 / 8))  # call to trian... function
#     turtle.end_fill()
#     turtle.up()
#     turtle.back(sizeHouse * (1 / 16))
#     turtle.right(90)
#
#
# # Shape Functions: certain repetitve shapes have been
# #   defined as functions allowing to reuse code
# def triangleShape(triEdge):  # Draws a triangle
#     turtle.right(30)
#     turtle.forward(triEdge)
#     turtle.right(120)
#     turtle.forward(triEdge)
#     turtle.right(120)
#     turtle.forward(triEdge)
#
#
# def quadrilateral(sqSide1, sqSide2):  # draw a square or rectangle
#     quadSide(sqSide1, sqSide2)  # draws 2 edges of the quadrilateral
#     quadSide(sqSide1, sqSide2)  # draws 2 edges of the quadrilateral
#
#
# def quadSide(sqSide1, sqSide2):  # draws 2 edges of the quadrilateral
#     turtle.forward(sqSide1)
#     turtle.right(90)
#     turtle.forward(sqSide2)
#     turtle.right(90)
#
#
# # Driver Code
# def main():
#     house(200, "LightGrey", "hotpink")  # user's screen resolution
#     # maybe too small to display house (for 1080p screens: max 200
#     # size)
#     turtle.done()  # Wait for user to end
#
#
# main()  # code driver called
#
#
