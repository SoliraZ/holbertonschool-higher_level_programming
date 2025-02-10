#!/usr/bin/python3
""" Module that writes a string to a text file (UTF8)
and returns the number of characters written """


def write_file(filename="my_first_file.txt", text=""):
    """ Function that writes a string to a text file (UTF8)
    and returns the number of characters written """
    with open(filename, 'w', encoding='utf-8') as my_file:
        my_file.write(text)
        return (len(text))
