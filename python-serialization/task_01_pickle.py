#!/usr/bin/python3
""" Task 01: Pickle Serialization """
import pickle


class CustomObject:
    """ CustomObject class """
    name = ""
    age = 0
    is_student = False

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        objects = self.__dict__
        for key, value in objects.items():
            print(f"{key}: {value}")

    def serialize(self, filename):
        with open(filename, 'wb') as my_file:
            pickle.dump(self, my_file)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as my_file:
                return pickle.load(my_file)
        except FileNotFoundError:
            return None
