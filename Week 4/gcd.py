"""
file: gcd.py
language: python3
author: ag9126@rit.edu Adit Garg
description: CSCI 141: hw04. The following code calculates GCD using recursion or iteration using user provided values
"""


def gcd_rec(a, b):
    """
        pre-conditions: a and b both are non-negative integers
        gcd_rec: Calculates GCD of a and b using recursion
        post-conditions: returns GCD
    """
    if b == 0:
        return a
    else:
        return gcd_rec(b, a % b)


def test_gcd_rec():
    """
        pre-conditions: None
        gcd_iter: Tests gcd_rec with a bunch of test cases
        post-conditions: returns GCD
    """
    print("GCD (5, 5) = ", gcd_rec(500, 5))
    print("GCD (23, 92) = ", gcd_rec(23, 92))
    print("GCD (345, 36) = ", gcd_rec(345, 36))
    print("GCD (24, 200) = ", gcd_rec(24, 200))
    print("GCD (3, 3) = ", gcd_rec(3, 3))
    print("GCD (50, 50) = ", gcd_rec(50, 50))
    print("GCD (3, 7) = ", gcd_rec(3, 7))
    print("GCD (13, 23) = ", gcd_rec(13, 23))
    print("GCD (25, 100) = ", gcd_rec(25, 100))
    print("GCD (100, 25) = ", gcd_rec(100, 25))


def gcd_iter(a, b):
    """
        pre-conditions: None
        gcd_iter: Tests gcd_iter with a bunch of test cases
        post-conditions: returns GCD
    """
    while b != 0:
        a, b = b, a % b
    return a


def test_gcd_iter():
    print("GCD (5, 5) = ", gcd_iter(500, 5))
    print("GCD (23, 92) = ", gcd_iter(23, 92))
    print("GCD (345, 36) = ", gcd_iter(345, 36))
    print("GCD (24, 200) = ", gcd_iter(24, 200))
    print("GCD (3, 3) = ", gcd_iter(3, 3))
    print("GCD (50, 50) = ", gcd_iter(50, 50))
    print("GCD (3, 7) = ", gcd_iter(3, 7))
    print("GCD (13, 23) = ", gcd_iter(13, 23))
    print("GCD (25, 100) = ", gcd_iter(25, 100))
    print("GCD (100, 25) = ", gcd_iter(100, 25))


def main():
    """
        pre-conditions: choice must be either 1 or 2, and the two numbers entered must be non-negative integers
        main: prompts user to choose one of the GCD functions and then prompts them for 2 non-negative integers
        post-conditions: None
    """
    print("Select the GCD function to use\n1. Recusrive\n2. Iterative")
    choice = int(input("Please select a function: "))
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    if choice == 1:
        gcd = gcd_rec(num1, num2)
    else:
        gcd = gcd_iter(num1, num2)
    print("\nGCD (", num1, ",", num2, ") = ", gcd)


if __name__ == "__main__":
    # Runs the tester functions and the main function
    test_gcd_iter()
    print("\n")
    test_gcd_rec()
    print("\n")
    main()
