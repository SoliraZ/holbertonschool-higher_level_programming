#!/usr/bin/python3
""" Module that returns the JSON
representation of an object (string) """


import json


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for key in sorted(attrs):
            if key in self.__dict__:
                new_dict[key] = self.__dict__[key]
        return new_dict

    def reload_from_json(self, json):
        for key in json:
            setattr(self, key, json[key])
