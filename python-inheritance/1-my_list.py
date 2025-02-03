#!/usr/bin/python3
""" Module for MyList class."""


class MyList(list):
    """ Class that inherits from list."""
    def print_sorted(self):
        """ Method that prints the list, but sorted."""
        print(sorted(self))
