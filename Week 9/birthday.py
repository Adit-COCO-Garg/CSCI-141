"""
file: birthday.py
language: python3
author: ag9126@rit.edu Adit Garg
description: CSCI 141: hw07. The following code parses a file with birthdays
and finds the ones that occurred a certain number of times.

"""

# Importing modules and dependencies
from dataclasses import dataclass


@dataclass(frozen=True)
class Birthday:
    month: str
    day: int
    year: int


def build_dictionary(filename):
    """
    Preconditions:
    :param filename: filename must be a path to a valid text file with valid
        and aptly formatted birthdays
    build_dictionary: builds a dictionary of birthdays and creates a tally
    :return: dictionary with parsed birthday data
    """
    bd_counts = dict()
    with open(filename) as file:
        for line in file:
            birthday_fields = line.strip().split()
            month = birthday_fields[0]
            day = int(birthday_fields[1])
            year = int(birthday_fields[2])
            if Birthday(month, day, year) in bd_counts:
                bd_counts[Birthday(month, day, year)] += 1
            else:
                bd_counts[Birthday(month, day, year)] = 1
    return bd_counts


def birthdays_atleast(bd_counts, min_count):
    """
    pre-conditions:
    :param bd_counts: dictionary with tallied birthdays
    :param min_count: the threshold of minimum occurrences
    birthdays_atleast: finds birthdays that pass the threshold.
    :return returns the birthday objects that do pass
    """
    return [birthday for birthday, count in bd_counts.items() if count >=
            min_count]


def to_strings(lst):
    """
    Pre-conditions:
    :param lst: List of birthdays that occurred more times then the threshold
    to_strings: parses birthday data into a readable string
    :return: returns a list of readable strings
    """
    months = dict(JAN="1", FEB="2", MAR="3", APR="4", MAY="5", JUN="6", JUL="7",
                  AUG="8", SEP="9", OCT="10", NOV="11", DEC="12")
    # return ['{months[birthday.month]}/{birthday.day}/birthday.year' for
    #  birthday in lst] # this might be hard to read?
    str_lst = []
    for birthday in lst:
        a = birthday.month
        string_bday = [months[a] + "/" + str(birthday.day) + "/" +
                       str(birthday.year)]  # .append is faster then +=
        str_lst += string_bday
    return str_lst


def main():
    # Main function provided within the lab!
    bd_counts = build_dictionary("birthday20000.txt")
    min_count = int(input("Enter a minimum count: "))
    list_birthdays = birthdays_atleast(bd_counts, min_count)
    print("Birthdays occurred at least " + str(min_count) + " times:")
    print(list_birthdays)
    print()
    list_strings = to_strings(list_birthdays)
    print(list_strings)


if __name__ == '__main__':
    main()
