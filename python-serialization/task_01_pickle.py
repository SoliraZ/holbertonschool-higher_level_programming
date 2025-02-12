#!/usr/bin/python3
""" Task 01: Pickle Serialization """
import pickle


class CustomObject:
    """ CustomObject class """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """ Display the object """
        objects = self.__dict__
        for key, value in objects.items():
            print(f"{key}: {value}")

    def serialize(self, filename):
        """ Serialize the object """
        try:
            with open(filename, 'wb') as my_file:
                pickle.dump(self, my_file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """ Deserialize the object """
        try:
            with open(filename, 'rb') as my_file:
                return pickle.load(my_file)
        except Exception:
            return None
