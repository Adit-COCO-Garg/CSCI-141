import turtle


def square(color_parm):
    """

    :param color_parm:
    :return:
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

    :param line:
    :return:
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
    pre-conditions: Constants are defined, turtle, random, and pi from math
    is imported
    sketch: serves as a  container and initializer for the canvas and the
    the entire drawing
    post conditions: turtle ends at the edge of the last raindrops last ripples
    edge, and circumference is printed
    """
    turtle.setworldcoordinates(0, -800*1.2, 800*1.2, 0)
    turtle.hideturtle()
    turtle.up()
    turtle.setpos(800*0.1, -800*0.1)
    turtle.tracer(False)
    turtle.down()

def main():
    """

    :return:
    """
    file_name = input("Enter the song's file name!\nFile name: ")
    # turtle.speed(0)
    picture(file_name)
    turtle.done()


if __name__ == '__main__':
    main()
