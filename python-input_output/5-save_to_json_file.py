#!/usr/bin/python3
""" Module that writes an Object to a text file,
using a JSON representation """


import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file,
    using a JSON representation """
    with open(filename, 'w') as my_file:
        my_file.write(json.dumps(my_obj))
