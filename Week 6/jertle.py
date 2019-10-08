"""
jertle.py
YOUR DESCRIPTION AND NAME HERE
"""

# Notice that this program runs as is.
# It does not do anything, but that's OK.
# As you add functionality, add test functions that you call
#   instead of the main function.
# Then run main when you are ready to try some things in normal operation.
# (Remove this block of comments before submission.)

import sys
import time
import turtle

# Turtle Canvas Window Setup ######
#
WORLD_SIZE = 300  #
MARGIN = 10  #
WINDOW_SIZE = WORLD_SIZE + MARGIN  #
#
###################################

SLEEP_TIME = 5

# The Set of Jertle Commands #####################################
#
PENDOWN_CMD = "!1"  # No parameters                              #
PENUP_CMD = "!0"  # No parameters                              #
TURN_CMD = "o^"  # Parameter: angle, to the left, in degrees  #
FORWARD_CMD = "->"  # Parameter: number of units to move         #
CIRCLE_CMD = "()"  # Parameter: radius of circle                #
#
##################################################################


### PRE-DEFINED ERROR CODES ###################################
#
ILLEGAL_COMMAND = 1  # Unrecognized command string            #
MISSING_ARGUMENT = 2  # More arguments needed for this command #
NO_ARG_END = 3  # Can't find the matching closing brace  #


#
###############################################################


def error(msg, e_code):
    """
    A fatal error has occurred.
    Print an error message and end the program.
    :param msg: the string message to print before ending the program
    :param e_code: the integer error code with which the program exits
    """
    print(msg, file=sys.stderr)
    sys.exit(e_code)


def initialize():
    """
    Set up the turtle world.
    :return: None
    """
    turtle.setup(WINDOW_SIZE, WINDOW_SIZE)
    turtle.setworldcoordinates(-MARGIN, -MARGIN, WORLD_SIZE, WORLD_SIZE)


def main():
    """
    Read Jertle program strings from a file and execute them.
    The file is provided by the user when this program runs.
    Stop when end of file is reached.
    :return: None
    """
    file_path = input("Jertle File?")
    file = open(file_path)
    interpreter(file)
    file.close()
    turtle.done()


def interpreter(file):
    for line in file:
        initialize()
        line = line.strip()
        while len(line) >= 2:
            if line[0] + line[1] == PENDOWN_CMD:
                line = line[2:]
                turtle.pendown()
            elif line[0] + line[1] == PENUP_CMD:
                line = line[2:]
                turtle.penup()
            elif line[0] + line[1] == TURN_CMD:
                try:
                    value, line = line_parser(line)
                    value = float(value)
                except TypeError:
                    error("Can't find the matching closing brace", NO_ARG_END)
                else:
                    turtle.left(value)
            elif line[0] + line[1] == FORWARD_CMD:
                try:
                    value, line = line_parser(line)
                    value = float(value)
                except TypeError:
                    error("Can't find the matching closing brace", NO_ARG_END)
                else:
                    turtle.forward(value)
            elif line[0] + line[1] == CIRCLE_CMD:
                try:
                    value, line = line_parser(line)
                    value = float(value)
                except TypeError:
                    error("Can't find the matching closing brace", NO_ARG_END)
                else:
                    turtle.circle(value)
            else:
                error("Unrecognized command string", ILLEGAL_COMMAND)


def line_parser(line):
    command = 0
    line = line[2:]
    if line[0] == "{":
        i = 0
        found = False
        while i < len(line) and line[i] != "":
            if line[i] == "}":
                found = True
                break
            i += 1
        if found:
            command = line[1:i]
            line = line[i+1:]
        else:
            error("Can't find the matching closing brace", NO_ARG_END)
    else:
        error("More arguments needed for this command", MISSING_ARGUMENT)
    print(command)
    return command, line


if __name__ == "__main__":
    main()
