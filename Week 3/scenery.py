"""
file: scenery.py
language: python3
author: ag9126@rit.edu Adit Garg
description: CSCI 141: Lab02. The following code
Draws a scenery with 2 houses and 1 tree. All with params and reusable
fruitful functions
"""

# Import modules/dependencies
import turtle
import math


def canvas_creat(house_w, house_l):
    """
    pre-conditions: For the program to function and display content properly,
        pass in the largest house width and length as the params.
    canvas_creat: Defines default canvas size and inits coordinates
    post-conditions: none
    """
    turtle.setup(width=8 * house_w, height=4 * house_l, startx=0,
                 starty=0)
    turtle.up()
    turtle.setx(-.5 * house_w)
    turtle.sety(-1 * house_l)


def draw_rec_poly(width, height, color):
    """
    pre-conditions: Width a number pref. int, height a number pref. int, color
        apt python color val.
    draw_rec_poly: Draws a rectangle according to the dimensions specified and
        fills it with the color specified (outlines too)
    post-conditions: turtle.up and ends where it started.
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
    """
    pre-conditions: Width a number pref. int, height a number pref. int
    draw_two_windows: Draws 2 windows according to the dimensions specified
        and fills it a blue-ish color that is supposed to represent a window
    post-conditions: turtle.up and ends where it started.
    """
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
    """
    pre-conditions: Width a number pref. int, height a number pref. int
    draw_four_windows: Draws 4 windows according to the dimensions specified
        and fills it a blue-ish color that is supposed to represent a window.
        This only occurs when the ratio of length to width exceeds 1. This
        function improves reusability and makes code more readable.
    post-conditions: turtle.up and ends where it started.
    """
    draw_two_windows(width, height / 2)
    turtle.left(90)
    turtle.forward(height / 2)
    turtle.right(90)
    draw_two_windows(width, height / 2)
    turtle.left(90)
    turtle.back(height / 2)
    turtle.right(90)


def draw_roof(base, angle, color):
    """
    pre-conditions: base a number pref. int, enter the same value as that of
        the house for best result. otherwise it would look like modern art.
        angle - degrees
        color - python color val
    draw_roof_windows: Draws a roof that sits on top of the house. Note: Use
        the same base length as that of the house for best results or else
        it might become modern art.
    post-conditions: turtle.up and ends where it started.
    """
    turn_angle = (180 - angle) / 2
    isosceles_tri_side = (base * 0.5) / math.cos(math.radians(turn_angle))
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(base)
    turtle.left(180 - turn_angle)
    turtle.forward(isosceles_tri_side)
    turtle.left(180 - angle)
    turtle.forward(isosceles_tri_side)
    turtle.left(180 - turn_angle)
    turtle.end_fill()
    turtle.up()


def draw_house(width_house, height_house, angle_roof, color_wall, color_roof):
    """
    pre-conditions:
        width_house = int num pref.
        height_house = int num pref.
        angle_roof = degrees
        color_wall = python color val
        color_roof = python color val
    draw_house: draws a house using params defined
    post-conditions: turtle.up and ends where it began
    """
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
    turtle.back(4 * width_house / 10)
    turtle.left(90)
    turtle.forward(height_house)
    turtle.right(90)
    draw_roof(width_house, angle_roof, color_roof)
    turtle.left(90)
    turtle.back(height_house)
    turtle.right(90)
    return area_sum


def draw_tree(tree_width, tree_height):
    """
    pre-conditions: tree with is at least 1.5 times the height
        if not = modern art
    draw_tree: draws a tree ........
    post-conditions: turtle.up and ends where it began
    """
    draw_rec_poly(tree_width, tree_height, "saddle brown")  # Draw door
    turtle.left(90)
    turtle.forward(tree_height*0.9)
    turtle.right(90)
    turtle.forward(tree_width/2)
    turtle.down()
    turtle.color("yellow green")
    turtle.begin_fill()
    turtle.circle(tree_width*5.2)
    turtle.end_fill()
    turtle.up()
    turtle.back(tree_width/2)
    turtle.left(90)
    turtle.back(tree_height*.9)
    turtle.right(90)


def tester_func():
    """
    pre-conditions: none...
    tester_func: tests the program........
    post-conditions: none...
    """
    canvas_creat(300, 600)
    draw_rec_poly(250, 100, "light grey")
    draw_roof(100, 30, "red")
    draw_two_windows(100, 100)
    draw_house(250, 100, 60, "light grey", "dim gray")
    turtle.forward(400)
    draw_house(300, 600, 60, "light grey", "dim gray")
    turtle.back(800)
    draw_tree(20, 200)


def main():
    """
        pre-conditions: turtle and math lib imported.
            house_width * 11 should not exceed user's current screen width.
            house_height * 4 should not should not exceed user's current screen
            height.
            tree_width * 11 should not exceed user's current screen width.
            tree_height * 4 should not should not exceed user's current screen
            height.
            base * 11 should not exceed user's current screen width.
            doing so may result in canvas being too big too fit.
        main: Draws 2 houses (prints largest and smallest area) and a tree.
        post-conditions: none...
    """
    # turtle.tracer(False) # turn tracer on or off for testing
    # tester_func() #tester function
    canvas_creat(100, 200)  # insert the largest facade height and facade width
    facade_area_1 = draw_house(100, 100, 30, "light grey", "dim gray")
    turtle.forward(200)
    facade_area_2 = draw_house(150, 200, 30, "light grey", "dim gray")
    if facade_area_1 > facade_area_2:
        print("The area of the bigger facade = ", facade_area_1)
        print("The area of the smaller facade = ", facade_area_2)
    elif facade_area_1 < facade_area_2:
        print("The area of the bigger facade = ", facade_area_2)
        print("The area of the smaller facade = ", facade_area_1)
    else:
        print("Both facades have equal area", facade_area_2)
    turtle.back(400)
    draw_tree(10, 100)
    turtle.forward(200)
    turtle.done()


main()
