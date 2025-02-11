#!/usr/bin/python3
""" Task 00: Basic Serialization """
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, 'w') as my_file:
        json.dump(data, my_file)
    pass


def load_and_deserialize(filename):
    with open(filename, 'r') as my_file:
        return json.load(my_file)
    pass
