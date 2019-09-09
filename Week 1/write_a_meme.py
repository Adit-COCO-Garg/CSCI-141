"""
file: write_a_meme.py
language: python 3.7
author: ag9126@rit.edu Adit Garg
description: CSCI 141: lab01: typography. The following program
draws up a meme,  sadly there is no image :( to go along with it...
"""

# Import modules/dependencies
import turtle
import math

def draw_t():
    """
    Pre-conditions: turtle module imported
    drawT: Draws a T
    Post-conditions: turtle ends at bottom left of the character with pen up
    """
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(100)
    turtle.back(50)
    turtle.left(90)
    turtle.back(100)
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)

def draw_o():
    """
    Pre-conditions: turtle module imported
    draw_o: Draws O
    Post-conditions: turtle ends at bottom left of the character with pen up
    """
    turtle.down()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.penup()
    turtle.forward(100)

def draw_m():
    """
    Pre-conditions: turtle module imported
    draw_m: Draws M
    Post-conditions: turtle ends at bottom left of the character with pen up
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.back(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.penup()

def draw_h():
    """
    Pre-conditions: turtle module imported
    draw_h: Draws H
    Post-conditions: turtle ends at bottom left of the character with pen up
    """
    turtle.penup()
    turtle.forward(100)
    turtle.left(90)
    draw_t()
    turtle.down()
    turtle.back(100)
    turtle.right(90)
    turtle.up()

def draw_e():
    """
    Pre-conditions: turtle module imported
    draw_o: Draws E
    Post-conditions: turtle ends at bottom left of the character with pen up
    """
    turtle.penup()
    turtle.forward(100)
    turtle.left(90)
    draw_m()
    turtle.up()
    turtle.back(100)
    turtle.right(90)

def draw_a():
    """
    Pre-conditions: turtle module imported
    draw_a: Draws a
    Post-conditions: turtle ends at bottom left of the character with pen up
    """
    turtle.down()
    draw_h()
    turtle.pendown()
    turtle.left(90)
    turtle.down()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)


def draw_n():
    """
    Pre-conditions: turtle module imported
    draw_n: Draws n
    Post-conditions: turtle ends at bottom left of the character with pen up
    """
    turtle.down()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(math.sqrt(100**2+100**2))
    turtle.left(135)
    turtle.forward(100)

def setup_canvas():
    """
    Pre-conditions: turtle module imported
    setup_canvas: initializes the canvas
    Post-conditions: none ends
    """
    turtle.setup(1300, 200)
    turtle.setworldcoordinates(0, 0, 1300, 200)
    turtle.up()
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)

def tester_func():
    """
        Pre-conditions: turtle module imported
        tester_func: Draws out a bunch of letters and checks if all the
            functions that draw the letters are working properly
        Post-conditions: none ends
    """
    # -------- Uncomment to test functions ---------- #
    # draw_a()
    # draw_n()
    # draw_m()
    # draw_h()
    # draw_t()
    # draw_e()
    draw_o()

def main(): # Driver code
    """
    Pre-conditions: turtle module imported
    main: draws out a meme caption...
    Post-conditions: none ends
    """
    setup_canvas()
    # tester_func() # -- Tester Function
    draw_t()
    turtle.forward(20)
    draw_o()
    turtle.forward(20)
    draw_m()
    turtle.forward(50)
    draw_t()
    turtle.forward(20)
    draw_h()
    turtle.forward(20)
    draw_e()
    turtle.forward(50)
    draw_m()
    turtle.forward(20)
    draw_a()
    turtle.forward(20)
    draw_n()
    turtle.done()
main()
