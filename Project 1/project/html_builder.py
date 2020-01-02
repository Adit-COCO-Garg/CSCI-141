"""
Author: Adit Garg
CS Project 1
html_builder.py

An html builder that.
"""


# Importing modules and depend
import sys
import turtle
import fontview
import cs_queue
from color_checker import color_checker

# Global variables
CSS_DICT = dict()
HTML = ["<!DOCTYPE html><html><head><title>", "</title>",
        "</head><body><h1>", "</body></html>"]
ARGUMENTS = ["!new_paragraph", "!title", "!image"]


def make_html():
    """
    pre-conditions: None
    Creates an html file up until the first header tag (wizard mode)
    :return: html file reference
    """
    html = open("index.html", "w+")
    html.write(HTML[0])
    title = input("What is the title of your website? ")
    html.write(title + HTML[1])
    styles_setup()
    css = css_maker()
    for line in css:
        html.write(line.strip())
    html.write(HTML[2]+title+"</h1>")
    return html


def file_parser(filename):
    """
    pre-conditions: filename must be a valid filepath to a valid text file
    :param filename: str
    reads in a file and builds a queue of commands
    :return: returns the queue of commands
    """
    commands = cs_queue.make_empty_queue()
    file = open(filename)
    para = False
    title = None
    paragraph = ""
    for line in file:
        line = line.strip()
        if title is None:
            title = "something"
            cs_queue.enqueue(commands, line)
        elif line == "" or line[0] != "!":
            para = True
            paragraph += line
        else:
            if para:
                cs_queue.enqueue(commands, paragraph)
                para = False
            cs_queue.enqueue(commands, line)
    file.close()
    return commands


def make_paragraph(text):
    """
    makes a paragraph (p tag)
    :param text: str
    :return: p tag
    """
    return "<p>" + text + "</p>"


def make_header(text):
    """
        makes a heading (h2 tag)
        :param text: str
        :return: h2 tag
    """
    return "<h2>" + text + "</h2>"


def make_image(img):
    """
        makes a img (h2 tag)
        :param img: array or str
        :return: img tag
    """
    if len(img) == 2:
        return "<img src=\"" + img[0] + "\" alt=\"" + img[
            0] + "\"> class = \"center\" width=\""+img[1]+"\">"
    elif len(img) == 3:
        return "<img src=\"" + img[0] + "\" alt=\"" + img[
            0] + "\"> class = \"center\" width=\""+img[1]+"\" height=\""+img[
            2]+"\">"
    else:
        img = [img]
        return "<img src=\"" + img[0] + "\" alt=\"" + img[0] + "\"> class = " \
                                                               "\"center\">"


def styles_setup():
    """
    sets up the style variables
    preconditions: none
    :return: none
    """
    valid = False
    while not valid:
        CSS_DICT["@BACKCOLOR"] = input("Background Color\nChoose the color: ")
        valid = color_checker(CSS_DICT["@BACKCOLOR"])
        if not valid:
            print("Illegal color value")
    valid = False
    while not valid:
        font_view = input("You will now choose a font.\nDo you want to see "
                          "what the fonts look like? [yes]")
        if font_view.lower()[0] == "y":
            fontview.runner()
            valid = True
        elif font_view.lower()[0] == "n":
            valid = True
        else:
            print("Illegal input")
    valid = False
    while not valid:
        CSS_DICT["@FONTSTYLE"] = input("Choose a font by its number.\n"
                                       "0: Arial, size 16\n"
                                       "1: Comic Sans MS, size 16\n"
                                       "2: Lucida Grande, size 16\n"
                                       "3: Tahoma, size 16\n"
                                       "4: Verdana, size 16\n"
                                       "5: Helvetica, size 16\n"
                                       "6: Times New Roman, size 16\n")
        if CSS_DICT["@FONTSTYLE"].isdigit():
            CSS_DICT["@FONTSTYLE"] = int(CSS_DICT["@FONTSTYLE"])
            if 0 <= CSS_DICT["@FONTSTYLE"] <= 6:
                valid = True
        else:
            print("illegal input")
    valid = False
    while not valid:
        CSS_DICT["@FONTCOLOR"] = input("Paragraph Text Color\nChoose the color: ")
        valid = color_checker(CSS_DICT["@FONTCOLOR"])
        if not valid:
            print("Illegal color value")
    valid = False
    while not valid:
        CSS_DICT["@HEADCOLOR"] = input("Heading Text Color\nChoose the color: ")
        valid = color_checker(CSS_DICT["@HEADCOLOR"])
        if not valid:
            print("Illegal color value")


def css_maker():
    """
    creates style tag using style variables
    pre-conditions: there is a valid style_template.txt
    :return: style
    """
    css_template = open("style_template.txt")
    css = ""
    for line in css_template:
        for css_property in CSS_DICT.keys():
            if css_property in CSS_DICT.keys():
                line = line.replace(css_property, str(CSS_DICT[css_property]))
        css += line
    css_template.close()
    return css


def para_cl(html):
    """
    creates a paragraph using the wizard tool
    :param html: html file ref
    :return: none
    """
    para_bool = True
    while para_bool:
        valid = False
        while not valid:
            para_bool = input("Do you want to add a paragraph? [yes]")
            if para_bool.lower()[0] == "y" or para_bool == "":
                h2 = input("Title of your paragraph\n")
                html.write(make_header(h2))
                p = input("Content of your paragraph (single line)\n")
                html.write(make_paragraph(p))
                valid = True
                img_cl(html)
            elif para_bool.lower()[0] == "n":
                valid = True
                para_bool = False
            else:
                print("Illegal input")


def img_cl(html):
    """
    creates a img
    :param html: html file ref
    :return: none
    """
    img_bool = True
    while img_bool:
        valid = False
        while not valid:
            img_bool = input("Do you want to add images? [yes]")
            if img_bool.lower()[0] == "y":
                valid = True
                img = input("Image File Name: ")
                html.write(make_image(img))
            elif img_bool.lower()[0] == "n" or img_bool == "":
                valid = True
                img_bool = False
            else:
                print("Illegal input")


def wizard_mode():
    """
    pre-conditions: none
    creates a html file using the wizard
    :return: none
    """
    html = make_html()
    para_cl(html)
    html.write(HTML[3])
    html.close()


def wiz_html(filename):
    """
    creates html files using prdefined params
    :param filename: existing valid filepaths (text)
    :return: none
    """
    commands = file_parser(filename)
    filename_ext = filename[:filename.find(".")]
    html = open(filename_ext + ".html", "w+")
    title = cs_queue.dequeue(commands)
    html.write(HTML[0] + title + HTML[1])
    styles_setup()
    css = css_maker()
    for line in css:
        html.write(line.strip())
    html.write(HTML[2] + title + "</h1>")
    body_parser(commands, html)
    html.write(HTML[3])
    html.close()


def body_parser(commands, html):
    """
    parses the body  and creates body content based on commands queue
    :param commands: queue
    :param html: a file reference.
    :return:
    """
    if commands is None:
        html.write(HTML[3])
        return None
    else:
        line = cs_queue.dequeue(commands)
        if "!new_paragraph" in line:
            line = cs_queue.dequeue(commands)
            if "!title" in line:
                h2 = line[7:]
                h2 = make_header(h2)
                html.write(h2)
            p = make_paragraph(cs_queue.dequeue(commands))
            html.write(p)
            return body_parser(commands, html)
        elif "!image" in line:
            img = line[7:]
            img = img.split(" ")
            img = make_image(img)

            html.write(img)
            return body_parser(commands, html)


if __name__ == '__main__':
    if 1 < len(sys.argv):
        for i in range(1, len(sys.argv)):
            wiz_html(sys.argv[i])
    else:
        wizard_mode()



