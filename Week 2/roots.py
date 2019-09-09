"""
file: roots.py
language: python 3.7
author: ag9126@rit.edu Adit Garg
description: CSCI 141: hw02: roots.py. The following program calculates roots
for a given value of a, b, and c. It determines the discriminant and based upon
it prints the number of roots and the roots themselves - if any.
"""

# Import modules/dependencies
import math


def quadratic_roots(a, b, c):
    """
    pre-conditions: Math library has to be imported
    quadratic_roots: Prints the quadratic equation, determines the discriminant,
        finds the number of possible roots - prints it - then prints the roots
        themselves, if any.
    post-conditions: none
    """
    discriminant = (b**2) - 4 * a * c
    print("Equation:  ", a, "x^2 + ", b, "x + ", c, " = 0", sep="")
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant))/(2*a)
        root2 = (-b - math.sqrt(discriminant))/(2*a)
        print("Two roots.")
        print("X = ", root1)
        print("X = ", root2)
    elif discriminant == 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        print("One root.")
        print("X = ", root1)
    else:
        print("No roots.")


def tester_func():
    """
    pre-conditions: None
    tester_func: Tests out random a, b, c to ensure all cases where there is
        0 roots, 1 root, and 2 roots for the quadratic equation
    post-conditions: none
    """
    quadratic_roots(1, 0, 0)
    quadratic_roots(2, -11, -21)
    quadratic_roots(-3, -1, -4)
    quadratic_roots(4, 1, 4)
    # quadratic_roots(0, 0, 0) a = 0 throws error
    quadratic_roots(25, -5, 25)
    quadratic_roots(-1, -5, -5)
    quadratic_roots(-1, 6, -8)
    quadratic_roots(200, -200, 200)
    quadratic_roots(9, 12, 4)
    quadratic_roots(1, -2, -4)
    quadratic_roots(76, 56, 3)


def main():
    """
    pre-conditions: Math library has to be imported!
    main: Calls upon the tester function to test the functionality of the
        program
    post-conditions: none
    """
    tester_func()
    # quadratic_roots(a, b, c) # Insert desired values


main()
