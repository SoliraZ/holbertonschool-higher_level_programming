#!/usr/bin/python3
""" Module that returns the JSON representation of an object (string) """


import json


def class_to_json(obj):
    """ Function that returns the JSON representation of an object (string) """
    return (json.dumps(obj.__dict__))
