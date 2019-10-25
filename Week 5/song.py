"""
file: songs.py
language: python3
author: ag9126@rit.edu Adit Garg
description: CSCI 141: hw04. The following code asks user for a path to a
lyric file and then based on it creates a visualization of the lyrics
"""

#  Importing modules/dependencies
import turtle


def square(color_parm):
    """
    pre-conditions: 
    :param color_parm: color_param a valid python turtle color.
    square: Draws 10x10 square that's colored with the passed in color param
    post-condition: draws a colored square with turtle ending where it started
        with pen up.
    """
    turtle.down()
    turtle.color(color_parm)
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.forward(10)
        turtle.left(90)
    turtle.end_fill()
    turtle.up()


def paint_line(line):
    """
    pre-conditions: line should be a valid string 
    :param line: line must be less then 80 characters to draw the lyrics
        visualization properly
    paint_line: Draws each character in the lyric as a square with a color
        attributed to it
    post-conditions: Turtle ends at the last square's start position with pen up
    """
    for char in line:
        if ord(char) < 70:
            color_param = "orange"
        elif 70 <= ord(char) < 100:
            color_param = "deep pink"
        elif 100 <= ord(char) < 110:
            color_param = "indigo"
        elif 110 <= ord(char) < 122:
            color_param = "turquoise"
        elif 122 <= ord(char):
            color_param = "dark violet"
        square(color_param)
        turtle.forward(10)


def picture(file_name):
    """

    :param file_name:
    :return:
    """
    sketch()
    file = open(file_name)
    line_num = 1
    for line in file:
        line = line.strip()
        paint_line(line)
        turtle.setpos(800*0.1, -800*0.1-(10*line_num))
        line_num += 1

        # transition back

def sketch():
    """
    pre-conditions: turtle is imported
    sketch: serves as a  container and initializer for the canvas and the
    the entire drawing
    post conditions: turtle is put at the very beginning of the drawing
    """
    turtle.setworldcoordinates(0, -800*1.2, 800*1.2, 0)
    turtle.hideturtle()
    turtle.up()
    turtle.setpos(800*0.1, -800*0.1)
    turtle.tracer(False)
    turtle.down()

def main():
    """
    pre-conditions: turtle is imported, file_name - path must exist
    main: The program asks user to input the filename for the lyrics in the
        program's directory (path must exist)
    post conditions: the turtle is done drawing the visual representation for
        the lyrics.
    """
    file_name = input("Enter the song's file name!\nFile name: ")
    # turtle.speed(0)
    picture(file_name)
    turtle.done()


if __name__ == '__main__':
    main()
