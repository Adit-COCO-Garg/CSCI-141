"""
CSCI-141 Week 9: Dictionaries & Dataclasses
Lab: 07-BabyNames
Author: RIT CS
Auhtor: Adit Garg

This utility module is used by the main programs to perform the work on the
data and return the desired results.
"""

from dataclasses import dataclass
from operator import attrgetter, itemgetter
from typing import List

# the range of valid years of data
START_YEAR = 1880
END_YEAR = 2018

# indices into the name data when splitting by commas
NAME_INDEX = 0
GENDER_INDEX = 1
COUNT_INDEX = 2

# gender strings
FEMALE = 'F'
MALE = 'M'


def get_filename(year):
    """
    Returns a formatted string for the filename that is associated with a
    given year.
    :param year: the desired year
    :return: a string, e.g. 'yob1990.txt' if year is 1990
    """
    return f'yob{year}.txt'


"""
PROBLEM 1: tops_in_year
"""

@dataclass
class NameInfo:
    """
    A NameInfo structure is used to represent three pieces of data that are
    required by the tops_in_year main program.  For each name we want
    to record the gender and the total count of babies that were born
    in a particular year.
    """
    name: str     # baby's first name
    gender: str   # gender of baby, ('F' = female, 'M' = male)
    count: int    # total babies with the same name and gender born in a year


def get_tops_in_year(year, num=10):
    """
    For a particular year, find and return the top 'num' babies that were
    born in that year, sorted in descending order by counts.  By default
    'num' is 10.
    :param year: the year
    :param num: the top number of babies
    :return: a list of NameInfo objects containing the top babies for that
        year in descending order by count.
    """
    names = make_names_1(get_filename(year))
    names.sort(key=attrgetter("count"), reverse=True)
    return names[:num]

def make_names_1(filename):
    file = open(filename)
    names = []
    for line in file:
        line = line.strip().split(",")
        name = line[0]
        gender = line[1]
        count = int(line[2])
        info = NameInfo(name, gender, count)
        names.append(info)
    file.close()
    return names


"""
PROBLEM 2: top_name_year
"""


@dataclass
class NameCount:
    """
    A NameCount structure is used to store the information required by
    the top_name_year main program.  In the year given, the top baby
    name of the year by total count, combining both genders, is to be
    found and returned.
    """
    name: str           # baby's first name
    count: int          # total babies with the same name (combining genders) in a year
    percentage: float   # how popular was the name in relation to all babies born that year


def get_top_name_year(year):
    """
    For a given year, find and return the top name, combining both genders if
    a name appears as both female and male.
    :param year: the year
    :return: a NameCount object with the top name information
    """
    names = make_names_2(get_filename(year))
    max_val = 0
    total = 0
    for name, val in names.items():
        count = val[1]
        total += count
        if count > max_val:
            max_val = count
            max_name = name
    return NameCount(max_name, max_val, (max_val/total)*100)

def make_names_2(filename):
    """
    Creates a dictionary of data read from the file
    :param filename: a valid relative path to an existing file
    :return: dictionary
    """
    file = open(filename)
    names = dict()
    for line in file:
        line = line.strip().split(",")
        name = line[0]
        gender = line[1]
        count = int(line[2])
        if name in names:
            names[name][1] += count
            if names[name][0] != gender:
                names[name][0] = "M/F"
        else:
            names[name] = [gender, count]
    file.close()
    return names


"""
PROBLEM 3: top_10_years
"""


@dataclass
class TopNamesYear:
    """
    A TopNamesYear structure is used by the top_10_years main program in order to find
    the top 'num' names over a range of years by total count.  It stores the
    female and male list of top names (strings).
    """
    females: List[str]     # list of top female names in descending order
    males: List[str]       # list of top male names in descending order


def get_top_years(start_year, end_year, num=10):
    """
    For a range of years, find and return the top 'num' female and male babies
    born over that range, in descending order.  By default 'num' is 10.
    :param start_year: the starting year (assumed to be valid)
    :param end_year: the ending year (assumed to be valid)
    :param num: the number of top names for each gender to generate
    :return: a TopNamesYear that holds the top female and male names in
    separate lists of strings.
    """
    m_names = dict()
    f_names = dict()
    for year in range(start_year, end_year+1):
        names_obj1,names_obj2 = make_names_3(get_filename(year))
        for name, val in names_obj1.items():
            if name in m_names:
                m_names[name][1] += val[1]
            else:
                m_names[name] = val
        for name, val in names_obj2.items():
            if name in f_names:
                f_names[name][1] += val[1]
            else:
                f_names[name] = val
    lst_names = []
    for name, val in m_names.items():
        lst_names.append(NameInfo(name, val[0], val[1]))
    for name, val in f_names.items():
        lst_names.append(NameInfo(name, val[0], val[1]))
    lst_names.sort(key=attrgetter("count"), reverse=True)
    female_lst = []
    male_lst = []
    i = 0
    while len(female_lst) <= num:
        if lst_names[i].gender == "F":
            female_lst.append(lst_names[i].name)
        i += 1
    i = 0
    while len(male_lst) <= num:
        if lst_names[i].gender == "M":
            male_lst.append(lst_names[i].name)
        i += 1
    return TopNamesYear(female_lst, male_lst)


def make_names_3(filename):
    """
        Creates a dictionary of data read from the file
        :param filename: a valid relative path to an existing file
        :return: 2 dictionaries
        """
    file = open(filename)
    F_names = dict()
    M_names = dict()
    for line in file:
        line = line.strip().split(",")
        name = line[0]
        gender = line[1]
        count = int(line[2])
        if name in M_names and gender == "M":
            M_names[name][1] += count
        elif name in F_names and gender == "F":
            F_names[name][1] += count
        elif gender == "M":
            M_names[name] = [gender, count]
        elif gender == "F":
            F_names[name] = [gender, count]
    file.close()
    return M_names, F_names
