#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev = 0
        for i in roman_string:
            current = roman_dict.get(i, 0)
            if current > prev:
                result += current - 2 * prev
            else:
                result += current
            prev = current
        return (result)
    return (0)
