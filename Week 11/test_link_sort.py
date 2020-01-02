"""
file: test_link_sort.py
author: Adit Garg
description: tester for functions in linked_insort.py
"""

import linked_insort
from linked_code import LinkNode
from linked_code import reverse_rec


def read_file( fname ):
    """
       Open a file of containing one integer per line,
       prepend each integer to a linked sequence,
       and return the reverse of the sequence.
       :param fname: A string containing the name of the file
       :return: A linked list of the numbers in the file, ordered
                identically to how they are ordered in the file
    """
    file = open(fname)
    lnk = None
    for line in file:
        line = int(line.strip())
        if lnk is None:
            lnk = LinkNode(line, None)
            continue
        lnk = LinkNode(line, lnk)
    lnk = reverse_rec(lnk) #oof my list was reversed... couldn't use lists...
    return lnk




def main():
    """
       Read file, build sequence, print it, sort it, print result, and
       pretty-print both lists.
    """

    name = input( "Enter file name: " )
    if name == "":
        return

    original_s = read_file( name )
    print( "unsorted:", original_s )

    sorted_s = linked_insort.insort( original_s )

    print( "sorted:", sorted_s )

    print( "pretty printed original: ", end="")
    linked_insort.pretty_print( original_s )
    print( "pretty printed sorted: ", end="")
    linked_insort.pretty_print( sorted_s )


if __name__ == "__main__":
    main()