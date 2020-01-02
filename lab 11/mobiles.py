"""
file: mobiles.py
language: python3
author: CS.RIT.EDU
author: Adit Garg ag9126
description: Build mobiles using a tree data structure.
date: 10/2015, 11/2019
purpose: starter code for the tree mobiles lab
"""

############################################################
#                                                          #
#    IMPLEMENT THE STRUCTURE DEFINITIONS PER REQUIREMENTS, # 
#    AND                                                   #
#    IMPLEMENT THE MOBILE CREATION AND ANALYSIS FUNCTIONS. #
#        See the 'define structure here' text below,       #
#        the 'Create mobiles from mobile files' text,      #
#        and the heading 'mobile analysis functions'.      #
#                                                          #
#    (See also the 'pass' statements to replace.)          #
#                                                          #
############################################################

from dataclasses import dataclass
from typing import Union


############################################################
# structure definitions
############################################################

@dataclass
class Ball:
    """
    class Ball represents a ball of some weight hanging from a cord.
    field description:
    cord: length of the hanging cord in inches
    weight: weight of the ball in ounces (diameter of ball in a drawing)
    """
    cord: float
    weight: float

@dataclass
class Rod:
    """
    class Rod represents a horizontal rod part of a mobile with
    a left-side mobile on the end of a left arm of some length,
    and a right-side mobile on the end of a right arm of some length.
    In the middle between the two arms is a cord of some length
    from which the rod instance hangs.
    field description:
    leftmobile: subordinate mobile is a mobile type.
    leftarm: length of the right arm in inches
    cord: length of the hanging cord in inches
    rightarm: length of the right arm in inches
    rightmobile: subordinate mobile is a mobile type.

    An assembled mobile has valid left and right subordinate mobiles;
    an unassembled mobile does not have valid subordinate mobiles.
    """
    leftmobile: Union["Rod", Ball, str]
    leftarm: float
    cord: float
    rightarm: float
    rightmobile: Union["Rod", Ball, str]


#########################################################
# Create mobiles from mobile files
#########################################################

def read_mobile(file):
    """
    read_mobile : OpenFileObject -> Dictionary( Ball | Rod )
    read_mobile reads the open file's content and
    builds a mobile 'parts dictionary' from the specification in the file.
    The parts dictionary returned has components for assembling the mobile.
    If the mobile is a simple mobile, the returned value is
    a parts dictionary containing a Ball instance.
    If the mobile is complex, the returned value is a parts list of
    the Rod instance representing the top-most mobile component and
    the other parts.
    The connection point for each part is a string that identifies
    the key name of the part to be attached at that point.

    If there is an error in the mobile specification, then
    return an empty parts dictionary.

    # an example of the file format. 'B10' is key for the 10 oz ball.
    # blank lines and '#' comment lines are permitted.
    B10 40 10

    top B10 240 66 80 B30
    B30 55 30
    
    """
    mobile_parts = dict()
    valid_mobile = False
    for line in file:
        line = line.strip().split()
        if line[0] == "top":
            valid_mobile = True
        if "#" in line:
            for word in line:
                print(word, end=" ")
            print("\n")
        elif len(line) > 3:
            mobile_parts[line[0]] = Rod(line[1], float(line[2]), float(line[3]),
                                        float(line[4]), line[5])
        else:
            mobile_parts[line[0]] = Ball(float(line[1]), float(line[2]))
    if not valid_mobile:
        return dict()
    else:
        return mobile_parts


def construct_mobile(parts):
    """
    construct_mobile : Dictionary( Rod | Ball ) -> Ball | Rod | NoneType

    construct_mobile reads the parts to put together the
    mobile's components and return a completed mobile object.
    The construct_mobile operation 'patches entries' in the parts.

    The parts dictionary has the components for assembling the mobile.
    Each Rod in parts has a key name of its left and right
    subordinate mobiles.  construct_mobile reads the key to
    get the subordinate part and attach it at the slot where
    the key was located within the component.

    The top mounting point of the mobile has key 'top' in parts.

    If the completed mobile object is a simple mobile, then
    the top returned value is a Ball instance.
    If the completed mobile is a complex mobile, then
    the top returned value is a Rod instance.

    If the parts dictionary contains no recognizable mobile specification,
    or there is an error in the mobile specification, then 
    return None.
    """
    top = parts["top"]
    del parts["top"]

    if isinstance(top, Ball):
        return top

    elif isinstance(top, Rod):
        reference1 = top.rightmobile
        parts["top"] = parts[reference1]
        del parts[reference1]
        top.rightmobile = construct_mobile(parts)

        reference2 = top.leftmobile
        parts["top"] = parts[reference2]
        del parts[reference2]
        top.leftmobile = construct_mobile(parts)
        return top

    if top is None:
        return None


############################################################
# mobile analysis functions
############################################################

def is_balanced(the_mobile):
    """
    is_balanced : Mobile -> Boolean

    is_balanced is trivially True if the_mobile is a simple ball. 

    Otherwise the_mobile is balanced if the product of the left side
    arm length and the left side is approximately equal to the 
    product of the right side arm length and the right side, AND
    both the right and left subordinate mobiles are also balanced.

    The approximation of balance is measured by checking
    that the absolute value of the difference between
    the two products is less than 1.0.

    If the_mobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: the_mobile is a proper mobile instance.
    """
    if isinstance(the_mobile, Ball):
        return True
    elif isinstance(the_mobile, Rod):
        weight_left = weight(the_mobile.leftmobile) * the_mobile.leftarm
        weight_right = weight(the_mobile.rightmobile) * the_mobile.rightarm
        if abs(weight_left-weight_right) < 1.0:
            return is_balanced(the_mobile.leftmobile) and is_balanced(
                the_mobile.rightmobile)
        else:
            return False
    else:
        raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))


def weight(the_mobile):
    """
    weight : Mobile -> Number
    weight of the the_mobile is the total weight of all its Balls.

    If the_mobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: the_mobile is a proper mobile instance.
    """
    if isinstance(the_mobile, Ball):
        return the_mobile.weight
    elif isinstance(the_mobile, Rod):
        return weight(the_mobile.leftmobile) + weight(the_mobile.rightmobile)
    else:
        raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))

 
def height(the_mobile):
    """
    height : the_mobile -> Number
    height of the the_mobile is the height of all tallest side.

    If the_mobile is not valid, then produce an exception
    with the message 'Error: Not a valid mobile\n\t{mobile}',

    pre-conditions: the_mobile is a proper mobile instance.
    """
    if isinstance(the_mobile, Ball):
        return the_mobile.cord + the_mobile.weight
    elif isinstance(the_mobile, Rod):
        left_height = height(the_mobile.leftmobile)
        right_height = height(the_mobile.rightmobile)
        if left_height > right_height:
            return the_mobile.cord + left_height
        else:
            return the_mobile.cord + right_height
    else:
        raise Exception("Error: Not a valid mobile\n\t" + str(the_mobile))
