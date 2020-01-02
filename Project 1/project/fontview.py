"""
Author: Adit Garg
CS Project 1
fontview.py

displays font choices
"""

import turtle


def window_setup():
    """
    sets up window
    :return: none
    """
    turtle.setup(500, 500)
    turtle.setworldcoordinates(0, 154, 154, 0)



def write_everything():
    """
    displays available fonts
    :return:
    """
    turtle.pencolor('black')
    x = 30
    turtle.up()
    turtle.setpos(7, x)
    turtle.down()
    turtle.write('Arial, 14', font=("Arial", 14))
    x += 14
    turtle.up()
    turtle.setpos(7, x)
    turtle.down()
    turtle.write('Comic Sans MS, size 14', font=('Comic Sans MS', 14))
    x += 14
    turtle.up()
    turtle.setpos(7, x)
    turtle.down()
    turtle.write('Lucida Grande, size 14', font=('Lucida Grande', 14))
    x += 14
    turtle.up()
    turtle.setpos(7, x)
    turtle.down()
    turtle.write('Tahoma, size 14', font=('Tahoma', 14))
    x += 14
    turtle.up()
    turtle.setpos(7, x)
    turtle.down()
    turtle.write('Verdana, size 14', font=('Verdana', 14))
    x += 14
    turtle.up()
    turtle.setpos(7, x)
    turtle.down()
    turtle.write('Helvetica, size 14', font=('Helvetica', 14))
    x += 14
    turtle.up()
    turtle.setpos(7, x)
    turtle.down()
    turtle.write('Times New Roman, size 14', font=('Times New Roman', 14))
    turtle.done()


def runner():
    """
    runs the font view module  to display fonts
    :return: none
    """
    window_setup()
    turtle.tracer(False)
    write_everything()
    print("Close window to continue")

