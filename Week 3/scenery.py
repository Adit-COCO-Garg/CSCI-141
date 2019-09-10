"""
file: scenery.py
language: python3
author: ag9126@rit.edu Adit Garg
description: CSCI 141: Lab02. The following code
Draws a scenery
"""

# Import modules/dependencies
import turtle, math


def canvas_creat(house_w, house_l):
    # Screen variables and default turtle location defined.
    turtle.setup(width=8 * house_w, height=4 * house_l, startx=0,
                 starty=0)
    turtle.up()
    # turtle.setx(-50)
    # turtle.sety(-150)
    turtle.setx(-.5 * house_w)
    turtle.sety(-1 * house_l)


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
    return width * height


def draw_two_windows(width, height):
    turtle.forward(width / 10)
    turtle.left(90)
    turtle.forward(height / 2)
    turtle.right(90)
    turtle.down()
    draw_rec_poly(width / 5, height / 4, "cornflower blue")  # Draw Windows
    turtle.left(90)
    turtle.back(height / 2)
    turtle.right(90)
    turtle.forward(3 * width / 5)
    turtle.left(90)
    turtle.forward(height / 2)
    turtle.right(90)
    turtle.down()
    draw_rec_poly(width / 5, height / 4, "cornflower blue")  # Draw Windows
    turtle.left(90)
    turtle.back(height / 2)
    turtle.right(90)
    turtle.back(7 * width / 10)


def draw_four_windows(width, height):
    draw_two_windows(width, height / 2)
    turtle.left(90)
    turtle.forward(height / 2)
    turtle.right(90)
    draw_two_windows(width, height / 2)
    turtle.left(90)
    turtle.back(height / 2)
    turtle.right(90)


def draw_roof(base, angle, color):
    turn_angle = (180 - angle) / 2
    isosceles_tri_side = (base * 0.5) / math.cos(math.radians(turn_angle))
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(base)
    turtle.left(180-turn_angle)
    turtle.forward(isosceles_tri_side)
    turtle.left(180-turn_angle)
    turtle.forward(isosceles_tri_side)
    turtle.left(180-turn_angle)
    turtle.end_fill()
    turtle.up()
    # return 0.5 * base * isosceles_tri_side * math.degrees(math.sin(
    # turn_angle))


def draw_house(width_house, height_house, angle_roof, color_wall, color_roof):
    area_sum = 0
    area_sum += draw_rec_poly(width_house, height_house,
                              color_wall)  # Draw the literal house
    if height_house / width_house > 1:
        draw_four_windows(width_house, height_house)
        stories = 0.5
    else:
        draw_two_windows(width_house, height_house)
        stories = 1
    turtle.forward(2 * width_house / 5)
    draw_rec_poly(width_house / 5, height_house * 0.75 * stories,
                              "peru")  # Draw door
    turtle.back(4*width_house/10)
    turtle.left(90)
    turtle.forward(height_house)
    turtle.right(90)
    draw_roof(width_house, angle_roof, color_roof)

    # draw_roof(width, angle, color)


def tester():
    canvas_creat(300, 600)
    draw_house(300, 600, 60, "light grey", "dim gray")


def main():
    turtle.tracer(False)
    tester()
    turtle.done()


main()
