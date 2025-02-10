#!/usr/bin/python3
""" Module that reads a text file (UTF8) and prints it to stdout """


def read_file(filename="my_file_0.txt"):
    print(open(filename, "r").read())
