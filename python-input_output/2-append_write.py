#!/usr/bin/python3
""" Module that writes a string to a text file (UTF8)
and returns the number of characters written """


def append_write(filename="file_append.txt", text=""):
    """ Function that writes a string to a text file (UTF8)
    and returns the number of characters written """
    with open(filename, 'a', encoding='utf-8') as my_file:
        my_file.write(text)
        return (len(text))
