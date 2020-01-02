"""
ALex Iacob
ai9388@rit.edu
Project 1: HTML Builder
file: wizard_mode.py
"""

global STYLE_STRING


def make_style_into_string():
    with open('style_template.txt', "r")as file:
        for line in file:
            STYLE_STRING += line





def replace_tag(tag, replacement):
    if tag in STYLE_STRING:
        STYLE_STRING.replace(tag, replacement)


def verify_hexadecimal(hexa):
    if hexa in COLORS:
        return True
    else:
        illegal_characters = ['g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                              'z']
        hexa_list = []

        for char in hexa:
            hexa_list.append(char)

        for i in hexa_list:
            if hexa_list[0] != '#':
                return False
            elif len(hexa_list) > 7:
                return False
            elif i in illegal_characters:
                return False
        # valid hex code
        return True


######## declaring prompting functions ########
def prompt_title():
    title_content = input('What is the title of your website?\n')
    return title_content


def prompt_back_color():
    back_color_content = input("What color would you like the background to be?\n"
                               "Write the color's name or hexadecimal value as '#XXXXXX'.\n")
    if verify_hexadecimal(back_color_content):
        replace_tag('@BACKCOLOR', back_color_content)
    else:
        print('Invalid code, try again.')
        prompt_back_color()


def prompt_font_style():
    print("What font would you like to use? Type 0-6 once your choice has been made.\n"
          " 0: Arial \n 1: Comic Sans \n 2: Lucida Grande \n 3: Tahoma \n 4: Verdana \n"
          " 5: Helvetica \n 6: Times New Roman")
    write_fonts.main()
    font_style_content = input()

    if font_style_content == '0':
        font_choice = 'Arial'
    elif font_style_content == '1':
        font_choice = 'Comic Sans MS'
    elif font_style_content == '2':
        font_choice = 'Lucida Grande'
    elif font_style_content == '3':
        font_choice = 'Tahoma'
    elif font_style_content == '4':
        font_choice = 'Verdana'
    elif font_style_content == '5':
        font_choice = 'Helvetica'
    elif font_style_content == '6':
        font_choice = 'Times New Roman'
    else:
        print('Value not acceptable, please try again')
        prompt_font_style()

    print("You have chosen", font_choice)
    replace_tag('@FONTSTYLE', font_choice)


def prompt_paragraph_color():
    paragraph_color_content = input("What color would you like the paragraphs to be?\n"
                                    "Write the color's name or hexadecimal value as '#XXXXXX'.\n")
    if verify_hexadecimal(paragraph_color_content):
        replace_tag('@FONTCOLOR', paragraph_color_content)
    else:
        print('Invalid code, try again.')
        prompt_paragraph_color()


def prompt_heading_color():
    heading_color_content = input("What color would you like the headings to be?\n"
                                  "Write the color's name or hexadecimal value as '#XXXXXX'.\n")
    if verify_hexadecimal(heading_color_content):
        replace_tag('@HEADCOLOR', heading_color_content)
    else:
        print('Invalid code, try again.')
        prompt_paragraph_color()


def prompt_style():
    print('You will now choose a background color.')
    prompt_back_color()
    print('You will now chose a font style. Close the turtle graphics window to make your choice.')
    prompt_font_style()
    print('You will now choose the color of the paragraphs.')
    prompt_paragraph_color()
    print('You will now choose the color of the headings.')
    prompt_heading_color()


def prompt_headings():
    pass


def prompt_paragraphs():
    pass


def html_create():
    make_style_into_string()
    title = prompt_title()
    style = prompt_style()
    headings = prompt_headings()
    paragraphs = prompt_paragraphs()

    print(STYLE_STRING)

    root = Html(Head(title, style), Body(headings, paragraphs))
    return root


def main():
    return html_create()


if __name__ == '__main__':
    main()