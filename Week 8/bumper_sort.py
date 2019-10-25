"""
file: bumper_sort.py
language: python3
author: ag9126@rit.edu Adit Garg
description: CSCI 141: hw08. tallies values in the unsorted list using a
    tally list based on index and tallying them to construct a sorted list.
"""

import random
import time
from merge_sort import merge_sort
from quick_sort import quick_sort


def bumper_sort(lst, k):
    """
    Pre-conditions:
    :param lst: non-negative integers
    :param k: length of list + 1
    bumper sort: tallies values in the unsorted list using a tally list based on
        index and tallying them to construct a sorted list.
    :return: sorted list
    """
    data = lst
    hist = [0] * (k + 1)
    result = []
    for element in data:
        hist[element] += 1
    for i in range(len(hist)):
        for j in range(hist[i]):
            result += [i]
    return result

def tester():
    unsorted = [2, 5, 3, 0, 2, 3, 0, 3]
    print("Small list, unsorted: ", unsorted)
    print("Small list, bump-sorted: ", bumper_sort(unsorted, 5))
    unsorted = [random.randrange(0, 300) for i in range(1000)]
    print("Large list, unsorted: ", unsorted)
    print("Large list, bump-sorted: ", bumper_sort(unsorted, 300))


if __name__ == '__main__':
    tester()
    max_val = 300
    unsorted_1 = [random.randrange(0, max_val) for i in range(1000)]
    unsorted_2 = [random.randrange(0, max_val) for i in range(1000000)]
    times_small = [0] * 4
    times_large = [0] * 4

    # Small list: 1000 elements
    start_time = time.process_time()
    merge_sort(unsorted_1)
    end_time = time.process_time()
    times_small[0] = end_time-start_time

    start_time = time.process_time()
    quick_sort(unsorted_1)
    end_time = time.process_time()
    times_small[1] = end_time - start_time

    start_time = time.process_time()
    bumper_sort(unsorted_1, max_val)
    end_time = time.process_time()
    times_small[2] = end_time-start_time

    start_time = time.process_time()
    sorted(unsorted_1)
    end_time = time.process_time()
    times_small[3] = end_time - start_time

    # large list: 1,000,000 elements
    start_time = time.process_time()
    merge_sort(unsorted_1)
    end_time = time.process_time()
    times_large[0] = end_time - start_time

    start_time = time.process_time()
    quick_sort(unsorted_1)
    end_time = time.process_time()
    times_large[1] = end_time - start_time

    start_time = time.process_time()
    bumper_sort(unsorted_1, max_val)
    end_time = time.process_time()
    times_large[2] = end_time - start_time

    start_time = time.process_time()
    sorted(unsorted_2)
    end_time = time.process_time()
    times_large[3] = end_time - start_time


    print("\nSorting a randomized list of 1000 elements")
    print("merge_sort time:", times_small[0], " seconds")
    print("quick_sort time:", times_small[1], " seconds")
    print("bumper_sort time:", times_small[2], " seconds")
    print("sorted_sort time:", times_small[3], " seconds")

    print("\nSorting a randomized list of 1,000,000 elements")
    print("merge_sort time:", times_large[0], " seconds")
    print("quick_sort time:", times_large[1], " seconds")
    print("bumper_sort time:", times_large[2], " seconds")
    print("sorted time:", times_large[3], " seconds")

