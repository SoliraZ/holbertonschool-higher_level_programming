#!/usr/bin/python
""" Task 02: CSV Serialization """


import csv
import json


def convert_csv_to_json(csv_file):
    """ Convert CSV to JSON """
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            data = csv.DictReader(f)
            obj = [row for row in data]
        with open("data.json", 'w', encoding="utf-8") as f:
            json.dump(obj, f, indent=4)
        return True
    except (FileNotFoundError, csv.Error, EOFError, IOError, Exception) as e:
        print("Error: {}".format(e))
        return False
