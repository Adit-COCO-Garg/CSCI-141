"""
CSCI-141 Week 10
Lab: 8
File: dna.py
Auhtor: Adit Garg ag9126@rit.edu

This program enables a bunch of features that are available to play around
with dna sequences
"""

# importing modules/ dependencies
import linked_code
from linked_code import LinkNode


def convert_to_nodes(dna_string):
    """
    Coverts a dna string strand to a linked list
    :param dna_string: string
    :return: linked list
    """
    if dna_string == "":
        return None
    else:
        return LinkNode(dna_string[:1], convert_to_nodes(dna_string[1:]))


def convert_to_string(dna_seq):
    """
    converts the dna linked list to a string
    :param dna_seq: a linked list
    :return: string
    """
    if dna_seq is None:
        return ""
    else:
        return dna_seq.value + convert_to_string(dna_seq.rest)


def is_match(dna_seq1, dna_seq2):
    """
    computes if dna_seq1 matches dna_seq2
    :param dna_seq1: linked list
    :param dna_seq2: linked list
    :return: True or False (bool)
    """
    if dna_seq1 is None and dna_seq2 is None:
        return True
    elif dna_seq1 is None or dna_seq2 is None:
        return False
    elif dna_seq1.value != dna_seq2.value:
        return False
    elif dna_seq1.value == dna_seq2.value:
        return is_match(dna_seq1.rest, dna_seq2.rest)


def is_pairing(dna_seq1, dna_seq2):
    """
    computes if dna_seq1 and dna_seq2 form valid pairs with each base
    :param dna_seq1: linked list
    :param dna_seq2: linked list
    :return: True or False (bool)
    """
    if dna_seq1 is None and dna_seq2 is None:
        return True
    elif dna_seq1 is None or dna_seq2 is None:
        return False
    else:
        temp = (dna_seq1.value + dna_seq2.value)
        if ("A" in temp and "T" in temp) or ("G" in temp and "C" in temp):
            return is_pairing(dna_seq1.rest, dna_seq2.rest)
        else:
            return False


def is_palindrome(dna_seq):
    """
    checks if dna_seq is a palindrome
    :param dna_seq: linked list
    :return: True or False (bool)
    """
    return is_match(linked_code.reverse_iter(dna_seq), dna_seq)


def substitution(dna_seq1, idx, base):
    """
    substitutes a new base at a given index within the dna_seq
    :param dna_seq1: linked list
    :param idx: int
    :param base: string (1 character)
    :return: linked list
    """
    if dna_seq1 is None:
        raise IndexError("Out of range")
    elif idx is 0:
        return LinkNode(base, dna_seq1.rest)
    else:
        idx -= 1
        return LinkNode(dna_seq1.value, substitution(dna_seq1.rest, idx, base))


def insertion(dna_seq1, dna_seq2, index):
    """
    inserts dna_seq2 strand in dna_seq1 at a given index
    :param dna_seq1: linked list
    :param dna_seq2: linked list
    :param index: int
    :return: linked list
    """
    if index == 0:
        return linked_code.concatenate(dna_seq2, dna_seq1)
    elif dna_seq1 is None:
        raise IndexError("Index out of bounds")
    else:
        index -= 1
        return LinkNode(dna_seq1.value, insertion(dna_seq1.rest, dna_seq2, index))


def deletion(dna_seq, idx, segment_size):
    """
    deletes a strand of segment_size in dna_seq at a given index
    :param dna_seq:  linked list
    :param idx: int
    :param segment_size: int
    :return: linked list
    """
    if segment_size == 0:
        return dna_seq
    elif dna_seq is None:
        raise IndexError("Out of bounds deletion")
    elif idx == 0:
        segment_size -= 1
        return deletion(dna_seq.rest, idx, segment_size)
    else:
        idx -= 1
        return LinkNode(dna_seq.value, deletion(dna_seq.rest, idx,
                                                segment_size))


def duplication(dna_seq, idx, segment_size):
    """
    duplicates a strand of segment_size in dna_seq at a given index
    :param dna_seq:  linked list
    :param idx: int
    :param segment_size: int
    :return: linked list
    """
    len_dna = linked_code.length_iter(dna_seq)
    if segment_size == 0:
        return dna_seq
    elif idx + segment_size > len_dna:
        raise IndexError("Invalid duplication")
    else:
        # copy of after idx
        second = deletion(dna_seq, 0, idx)
        # copy of before idx
        first = deletion(dna_seq, idx, len_dna-idx)
        # copy of segment
        len_second = linked_code.length_iter(second)
        copy = deletion(second, segment_size, len_second-segment_size)
        # inset segment at end of first
        return linked_code.concatenate(first, linked_code.concatenate(copy,
                                                                      second))
