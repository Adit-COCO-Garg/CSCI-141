"""
A dataclass that represents "spots" on the skewer and functions that work
with it.

author: RITCS
author: << YOUR NAME HERE >>
"""

from dataclasses import dataclass
from typing import Union
from food import Food, CALORIES, VEGGIES

@dataclass
class KebabSpot:
    """
    Class: KebabSpot
    Description: This class is used to represent an individual
        spot on the skewer.  Each spot contains a Food 'item',
        and a reference to the 'next' spot.
    """
    item: Food
    next: Union[None, 'KebabSpot']


def spot_create(item, next):
    """
    Create a new food item spot on the skewer
    :param item (Food): new food item
    :param next: next spot
    :return: new spot
    """
    return KebabSpot(item, next)


def spot_name(spot):
    """
    Return the name of the food item in this spot.
    :param: spot (KebabSpot): the current spot on the skewer
    :return: food name
    """
    return spot.item.name

def spot_size(spot):
    """
    Return the number of elements from this KebabSpot instance to the end
    of the skewer.
    :param: spot (KebabSpot): the current spot on the skewer
    :return: the number of elements (int)
    """
    if spot is None:
        return 0
    else:
        return 1 + spot_size(spot.next)

def spot_has(spot, name):
    """
    Return whether there are is a food item from this spot to the end of
    the skewer.
    :param: spot (KebabSpot): the current spot on the skewer
    :param name: the name (string) being searched for.
    :return True if any of the spots hold a Food item that equals the
    name, False otherwise.
    """
    if spot is None:
        return False
    if spot_name(spot) == name:
        return True
    else:
        return spot_has(spot.next, name)

def spot_string_em(spot):
    """
    Return a string that contains the list of items in the skewer from
    this spot down, with a comma after each entry.
    :param: spot (KebabSpot): the current spot on the skewer
    :return A string containing the names of each of the Food items from
    this spot down.
    """
    constructed = False
    string = ""
    while not constructed:  # a modification of my pretty print in hw 10
        if spot is None:
            constructed = True
        elif spot.next is None:
            string += spot_name(spot)
            constructed = True
        else:
            string += spot_name(spot)+", "
            spot = spot.next
    return string

def spot_calories(spot):
    """
    finds calories of all items on the skewer
    :param spot: a kebab spot
    :return: cal (calories)
    """
    cal = 0
    while spot is not None:
        cal += CALORIES[spot_name(spot)]
        spot = spot.next
    return cal

def spot_vegan(spot):
    """
    finds if everything on the skewer is vegan or not
    :param spot: kebab spot
    :return: string which says whether kebab is vegan friendly or not
    """
    while spot is not None:
        if not spot_name(spot) in VEGGIES:
            return "Skewer is not vegan friendly"
        else:
            spot = spot.next
    return "Skewer is vegan friendly"