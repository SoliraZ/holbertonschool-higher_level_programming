#!/usr/bin/python3
""" Module that returns the JSON representation of an object (string) """


def class_to_json(obj):
    """ Function that returns the JSON representation of an object (string) """
    return obj.__dict__
