#!/usr/bin/python3
""" Module that adds all arguments to a Python list,
and then save them to a file """


import json
import sys


def load_from_json_file(filename):
    """ Function that creates an Object from a JSON file """
    with open(filename, 'r') as my_file:
        return (json.load(my_file))


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file,
    using a JSON representation """
    with open(filename, 'w') as my_file:
        my_file.write(json.dumps(my_obj))


try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

save_to_json_file(my_list, "add_item.json")
