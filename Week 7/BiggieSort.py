"""
file: biggiesort.py
language: python3
author: ag9126@rit.edu Adit Garg
description: CSCI 141: hw07. The following code asks user for a path to a
file with unsorted elements and then sorts them using the biggie sort algorithm

1. Insertion sort preforms better in the case where the list is already sorted
and in cases where the elements are not too far away from their sorted
position. For example 1,2,3,4,5,6,7 will be sorted in roughly 7 iterations
using insertion sort. However the same list will take biggie sort about 7! (
factorial) iterations.

2.This is due to the 2 for loops present in the biggie sort which
has to go around the entire list for as many elements that are present in
order to make sure that the items are sorted. Whereas in the insertion sort
items are swapped until they reach the same number or smaller or greater
depending on the order of the sorted elements using a while loop and this
is done until the main iterator reaches the last element and has no elements
left to sort. Therefore a sorted list will run for O(N) times for Insertion
sort - N being the number of elements, but biggie sort will run in polynomial
time.
"""


def biggie_sort(lst):
    """
    Preconditions:
    :param lst: lst is a single dimensional list of integers
    biggie_Sort: sorts a list of unsorted numbers into sorted numbers
    :return: a sorted list of integers
    """
    sorted_len = 0
    for i in range(len(lst) - sorted_len):
        swap(find_max(lst, sorted_len), (len(lst)-1) - sorted_len, lst)
        sorted_len += 1
    return lst


def find_max(lst, sorted_len):
    """
    Pre-Conditions:
    :param lst: A list of integers
    :param sorted_len: an integer less than or equal to the number of
    elements in the list.
    find_max: Finds a maximum value within the unsorted portion in the list
    and returns it's index.
    :return: returns index of the maximum value
    """
    max_val = 0
    max_index = (len(lst)-1) - sorted_len
    for i in range(len(lst)-sorted_len):
        if lst[i] > max_val:
            max_index = i
            max_val = lst[max_index]
    return max_index


def swap(max_index, srt_index, lst):
    """
    Preconditions:
    :param max_index: integer value less than or equal to the length of the list
    :param srt_index: integer value less than or equal to the length of the list
    :param lst: a list of integers
    swap: swaps values between indexes in the list
    :return None
    """
    lst[max_index], lst[srt_index] = lst[srt_index], lst[max_index]


def main():
    """
        Preconditions:
        file_name: File exists and has 1 integer number on each line
        main: Prompts user for file name/ path and then based upon that reads
        values into a list and passes it into biggie sort to get sorted and then
        prints the sorted list
        return none
        """

    file_name = input("Enter file name:  ")
    print("Sorting File: " + file_name)
    file = open(file_name)
    unsorted = []
    for line in file:
        unsorted += [int(line)]
    file.close()
    print("unsorted: ", unsorted)
    print("sorted: ", biggie_sort(unsorted))


if __name__ == '__main__':
    main()

