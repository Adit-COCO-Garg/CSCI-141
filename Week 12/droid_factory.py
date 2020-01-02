"""
Author: Adit Garg
CS HW 11
droid_factory.py

Simulates a droid factory based on droid parts!
"""

# Importing modules/ Dependencies
import sys
import node
import cs_queue
from dataclasses import dataclass


@dataclass()
class Droid:
    head: bool
    body: bool
    arms: bool
    legs: bool
    serial_number: int


def unload_onto_belt(filename, belt):
    """
    Unloads droid parts from a file onto a conveyor belt
    :param filename: existing and valid txt file with 1 part per line
    :param belt: a valid queue
    :return:
    """
    parts = open(filename)
    for part in parts:
        part = part.strip()
        cs_queue.enqueue(belt, part)
    parts.close()


def make_droid(serial_num, belt):
    """
    Creates a singular droid or returns none with apt. messages
    :param serial_num: 5 digit serial num
    :param belt: a queue
    :return: a droid
    """
    baby_droid = Droid(False, False, False, False, serial_num)
    print("Droid with serial number: ", serial_num, " is being assembled")
    assembled = baby_droid.head and baby_droid.arms and baby_droid.legs and \
        baby_droid.body
    count = 0
    while not assembled and not cs_queue.is_empty(belt) and count < belt.size:
        count += 1
        part = cs_queue.dequeue(belt)
        if part == "head" and not baby_droid.head:
            print("Attaching head. . .")
            baby_droid.head = True
        elif part == "body" and not baby_droid.body:
            print("Attaching body. . .")
            baby_droid.body = True
        elif part == "legs" and not baby_droid.legs:
            print("Attaching legs. . .")
            baby_droid.legs = True
        elif part == "arms" and not baby_droid.arms:
            print("Attaching arms. . .")
            baby_droid.arms = True
        else:
            print("Returning extra part:", part, "back to belt. . .")
            cs_queue.enqueue(belt, part)
        assembled = baby_droid.head and baby_droid.arms and baby_droid.legs \
            and baby_droid.body
    if not assembled:
        print("Ran out of parts, gotta ask Scotty to beam up more parts!")
        if count >= belt.size:
            print("ERROR: Belt has no parts left to finish the droid!")
        return None
    else:
        print("Droid was assembeled! Serial Num:", baby_droid.serial_number,
              "\n")
        return baby_droid


def make_all_droids(belt):
    """
    creates all the droids possible based on the parts available on the belt
    :param belt: queue
    :return: serial num of last bot - used to check for incorrect serial
    assignments
    """
    i = 10000
    if cs_queue.is_empty(belt):
        return 0
    while not cs_queue.is_empty(belt):
        test_val = make_droid(i, belt)
        if test_val is not None:
            i += 1
    print("All droids have been built! Time to watch star trek!")
    return i


def tester_1():
    """
    Tests missing args, and proper creation of a droid struct
    :return: none
    """
    try:
        Droid()  # This should fail
        print("Droid struct is improperly setup! FAIL")
    except:
        print("Pass")
    try:
        droid = Droid(False, False, False, False, 10000)
        fail = droid.body and droid.legs and droid.arms and droid.head
        if not fail:
            print("PASS!")
        else:
            print("Droid struct is improperly setup! FAIL")
    except:
        print("Droid struct is improperly setup! FAIL")


def tester_2():
    """
    Tests improper file read (split) and checks values are enqueued in order
    :return: none
    """
    conveyor_belt_test = cs_queue.make_empty_queue()
    unload_onto_belt("droid_parts_1.txt", conveyor_belt_test)
    if cs_queue.is_empty(conveyor_belt_test):
        print("FAIL: Empty queue, Improper file read")
    if cs_queue.front(conveyor_belt_test) != "head":
        print("FAIL: Improper read from file")

def tester_3():
    """
    Tests for empty belt, belt enough parts for multiple droids, and creation of
    droids along with proper dequeue and enqueue operations
    :return:
    """
    conveyor_belt_test = cs_queue.make_empty_queue()
    # check for empty conveyor belt
    test_val = make_droid(0, conveyor_belt_test)
    if test_val is None:
        print("PASS!")
    else:
        print("FAIL")
    unload_onto_belt("droid_parts_3.txt", conveyor_belt_test)
    # check for conveyor belt with multiple parts (enough for 3 droids)
    test_val = make_droid(0, conveyor_belt_test)
    if test_val is None:
        print("FAIL!")
    else:
        droid = test_val.arms and test_val.legs and test_val.body and \
            test_val.head
        if droid and test_val.serial_number == 0:  # Checks for valid droid
            # creation
            print("PASS!")
        else:
            print("FAIL!")
        if conveyor_belt_test.size == 8:  # Checks for proper dequeue and
            # enqueue operations: IN CASE OF UNNEEDED ITEMS IT SHOULD RETURN
            # TOTAL LINES IN FILE (EXCLUDING NEW LINE) - 4
            print("PASS!")
        else:
            print("FAIL!")
    conveyor_belt_test = cs_queue.make_empty_queue()
    for j in range(0, 4):
        cs_queue.enqueue(conveyor_belt_test, "head")
        cs_queue.enqueue(conveyor_belt_test, "body")
        cs_queue.enqueue(conveyor_belt_test, "body")
    droid = make_droid(0, conveyor_belt_test)
    if droid is None:  # Tests for situation where there are parts in the belt
        # but not the ones needed to finish a drone
        print("Pass")
    else:
        print("Fail")



def tester_4():
    """
    tests the loop, the serial num generation, and droid creation based on
    varied types of belts
    :return: none
    """
    conveyor_belt_test = cs_queue.make_empty_queue()
    test_val = make_all_droids(conveyor_belt_test)
    if test_val == 0: # Tests if belt is empty then no droids should be
        # created!
        print("PASS")
    else:
        print("FAIL")
    if conveyor_belt_test.size == 0:  # checks for improper droid creation
        # and improper belt operations
        print("PASS")
    else:
        print("FAIL")

    unload_onto_belt("droid_parts_3.txt", conveyor_belt_test)
    test_val = make_all_droids(conveyor_belt_test)
    if test_val-10000 == 1:  # Tests serial number generation for the droids
        print("PASS")
    else:
        print("FAIL")
    if conveyor_belt_test.size == 0:  # this is basically conducting task 3
        # tests again... checks if 3 droids are created and belt is empty.
        # This will determine if droids are being created as per the rules
        # and the belt is being updated too!
        print("PASS")
    else:
        print("fail")
    conveyor_belt_test = cs_queue.make_empty_queue()
    for j in range(0, 4):
        cs_queue.enqueue(conveyor_belt_test, "head")
        cs_queue.enqueue(conveyor_belt_test, "body")
        cs_queue.enqueue(conveyor_belt_test, "body")
    test_val = make_all_droids(conveyor_belt_test) # Tests if all the parts
    # in the queue are only traversed through once and apt. messages are
    # printed if there are parts present in the list but not the ones needed
    if test_val-10000 == 0:    # CHECKS IF SERIAL NUMBERS ARE BEING SET
        # properly, if there is a broken infinite loop, and only valid droids
        # are created
        print("PASS")
    else:
        print("FAIL")


if __name__ == '__main__':
    tester_1()
    tester_2()
    tester_3()
    tester_4()
    # if len(sys.argv) != 2:
    #     print("Usage: droid_factory.py filename_for_droid_parts")
    # else:
    #     conveyor_belt = cs_queue.make_empty_queue()
    #     unload_onto_belt(sys.argv[1], conveyor_belt)
    #     make_all_droids(conveyor_belt)
