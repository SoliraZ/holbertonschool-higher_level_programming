#!/usr/bin/python3
""" Module that reads a text file (UTF8) and prints it to stdout """


def read_file(filename="my_file_0.txt"):
    """ Function that reads a text file (UTF8) and prints it to stdout """
    with open(filename, 'r', encoding='utf-8') as my_file:
        print(my_file.read(), end="")
