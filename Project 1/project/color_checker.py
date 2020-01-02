"""
Author: Adit Garg
CS Project 1
color_checker.py

A color checker
"""

VALID_COLORS = {'peachpuff', 'slateblue', 'powderblue', 'lightcyan',
                'chartreuse','moccasin', 'mediumseagreen', 'lawngreen',
                'seagreen', 'mintcream', 'azure', 'goldenrod', 'lightblue',
                'firebrick', 'lightseagreen', 'chocolate', 'yellowgreen',
                'darkolivegreen', 'violet', 'ivory', 'sandybrown', 'wheat',
                'mediumvioletred', 'bisque', 'lightgreen', 'cyan', 'hotpink',
                'gray', 'indianred ', 'antiquewhite', 'royalblue', 'yellow',
                'indigo ', 'lightcoral', 'darkslategrey', 'sienna',
                'lightslategray', 'mediumblue', 'red', 'khaki', 'darkviolet',
                'mediumorchid', 'darkblue', 'lightskyblue', 'turquoise',
                'lightyellow', 'grey', 'whitesmoke', 'blueviolet', 'orchid',
                'mediumslateblue', 'darkturquoise', 'coral', 'forestgreen',
                'gainsboro', 'darkorange', 'cornflowerblue',
                'lightsteelblue',  'plum', 'lavender', 'palegreen',
                'darkred',  'dimgray', 'floralwhite', 'orangered', 'oldlace',
                'darksalmon', 'lavenderblush', 'darkslategray', 'tan',
                'cadetblue', 'silver', 'tomato', 'darkkhaki', 'slategray',
                'maroon', 'olive', 'deeppink', 'linen', 'magenta', 'crimson',
                'mistyrose', 'lime', 'saddlebrown', 'blanchedalmond',
                'black', 'snow', 'seashell', 'darkcyan', 'gold',
                'midnightblue',  'darkgoldenrod', 'palevioletred', 'fuchsia',
                'teal', 'lightpink', 'darkgrey', 'mediumspringgreen',
                'aquamarine', 'lightsalmon', 'navajowhite', 'darkgreen',
                'burlywood', 'rosybrown', 'springgreen', 'purple',
                'olivedrab',  'lightslategrey', 'orange', 'aliceblue',
                'mediumaquamarine', 'navy', 'salmon', 'rebeccapurple',
                'darkmagenta', 'limegreen', 'deepskyblue', 'pink',
                'mediumpurple', 'skyblue', 'aqua', 'blue', 'slategrey',
                'darkslateblue', 'honeydew', 'darkseagreen', 'paleturquoise',
                'brown', 'thistle', 'lemonchiffon', 'peru', 'cornsilk',
                'papayawhip', 'green', 'lightgoldenrodyellow',
                'mediumturquoise', 'steelblue', 'lightgray', 'lightgrey',
                'beige', 'palegoldenrod', 'darkgray', 'white', 'ghostwhite',
                'dodgerblue', 'greenyellow', 'dimgrey', 'darkorchid'}


def color_checker(color):
    """
    checks a string if its a valid color or not
    :param color: str
    :return: bool
    """
    color = color.lower().strip()
    if color[0] == "#":
        hex_count = 1
        color = color[1:]
        for char in color:
            if (48 <= ord(char) <= 57 or 97 <= ord(char) <= 122) and \
                    hex_count < 7:
                hex_count += 1
            else:
                break
        return False
    if color in VALID_COLORS:
        return True
