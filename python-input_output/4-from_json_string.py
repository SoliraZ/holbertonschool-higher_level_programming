#!/usr/bin/python3
""" Module that returns the JSON representation of an object (string) """


import json


def from_json_string(my_str):
    """ Function that returns the JSON representation of an object (string) """
    return (json.loads(my_str))
