"""
file: lasers.py
language: python3
author: ag9126@rit.edu Adit Garg
description: CSCI 141: lab06. Based on a puzzle present in the file passed,
the program finds
    optimal laser tower placements.
"""

import sys
import insertion

def read_func(filename):
    """
    Pre-conditions:
    :param filename: filename must be a path to a file with 1 line of list of
    integers
    read_func: reads a file and returns the data read in a list
    post-conditions:
    :return: puzzle: a list of integer numbers
    """
    file = open(filename)
    for line in file:
        puzzle = [int(num) for num in line.split()]
    return puzzle

def sort(lasers):
    """
    Preconditions:
    :param lasers: a list of laser tuples
    sort: sorts the list based on the laser's scores [ascending]
    post-conditions:
    :return: a sorted list of laser placements with the highest score
    """
    return insertion.insertion_sort(lasers)

def find_towers_up(lst):
    """
    Pre-conditions:
    :param lst: A list of integers
    find_towers_up: Finds all possible solutions for the laser placements
    post-conditions:
    :return: a list of tuples that represents lasers
    """
    up_lasers = []
    for i in range(1, len(lst)-2):
        up_lasers += [(lst[i-1]+lst[i]+lst[i+1]+lst[i+2],i,"upward")]
    return up_lasers

def find_towers_down(lst):
    """
        Pre-conditions:
        :param lst: A list of integers
        find_towers_down: Finds all possible solutions for the laser placements
        post-conditions:
        :return: a list of tuples that represents lasers
        """
    down_lasers = []
    for i in range(2, len(lst)-1):
        down_lasers += [(lst[i-2]+lst[i-1]+lst[i]+lst[i+1],i,"downward")]
    return down_lasers

def place_lasers(lst, laser_num):
    """
    Pre-conditions:
    :param lst: a list of tuples that represents tuples. Must be sorted [
    ascending]
    :param laser_num: An integer value for number of lasers that require
    placement
    place_lasers: Finds the solution to the laser placement problem
    Post-conditions:
    :return: returns a list of tuples representing lasers based on how many
    lasers were asked to be placed.
    """
    opt_lasers = []
    occupied_locations = []
    for i in range(1,len(lst)):
        if lst[-i][1] not in occupied_locations:
            opt_lasers += [lst[-i]]
            occupied_locations+=[lst[-i][1]]
            if len(occupied_locations) == laser_num:
                break
    return opt_lasers

def main():
    """
    pre-conditions: File passed must exist. num-towers must be a non-negative
    integer.
    main: Based on a puzzle present in the file passed, the program finds
    optimal laser tower placements.
    post-conditions: none
    :return: none
    """
    if len(sys.argv) !=3:
        print("Usage: lasers.py laser-file num-towers")
    else:
        lst = read_func(sys.argv[1])
    list_string=""
    for i in range(len(lst)):
        list_string += str(lst[i]) + " "
    print(list_string)
    print(sys.argv[2], " lasers")
    positions_up = find_towers_up(lst)
    positions_down = find_towers_down(lst)
    optimal_lst = sort(positions_up+positions_down)
    laser_locations = place_lasers(optimal_lst, int(sys.argv[2]))
    for i in range(len(laser_locations)):
        print("Centered at location ",laser_locations[i][1]," facing ",
              laser_locations[i][2], " scoring ",laser_locations[i][0] )

if __name__ == '__main__':
    main()