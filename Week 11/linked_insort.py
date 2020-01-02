"""
file: linked_insort.py
author: Adit Garg
description: homework 10
The following lab sorts a linked list using insertion sort (ascending) and
provides functionality to pretty print it!
"""

import linked_code
from linked_code import LinkNode


def insert(value, lnk):
    """
    Put the value in the proper spot in the linked list to keep it sorted.
    New nodes are created.
    :param value: the value to add to the sequence of values in the list
    :param lnk: the node at the head of the list
    :return: a (partially) new linked list with the value inserted
    :pre: the list headed by lnk is sorted.
    :post: the link returned refers to a list that is sorted.
    """
    if lnk is None:
        return LinkNode(value, None)
    elif lnk.value < value:
        return LinkNode(lnk.value, insert(value, lnk.rest))
    else:
        return LinkNode(value, lnk)


def insort(lnk):
    """
    Return a copy of a linked list where all the values are sorted,
    with the lowest value at the head.
    :param lnk: the node at the head of the provided list
    :return: the head node of the sorted linked list
    """
    sorted_lnk = None
    while lnk is not None:
        sorted_lnk = insert(lnk.value, sorted_lnk)
        lnk = lnk.rest
    return sorted_lnk


def pretty_print(lnk):
    """
    Print the contents of a linked list in standard Python format.
    [value, value, value] (Note the spaces.)
    :param lnk: the node at the head of the provided list
    :return: None
    """
    constructed = False
    string = "["
    while not constructed:
        if lnk is None:
            string += "]"
            constructed = True
        elif lnk.rest is None:
            string += str(lnk.value)+"]"
            constructed = True
        else:
            string += str(lnk.value)+", "
            lnk = lnk.rest
    print(string)
