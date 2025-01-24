#!/usr/bin/python3
"""
Defines a function that prints a text
with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text (str): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    for char in ".?:":
        text = (char + "\n\n").join(
            [line.strip() for line in text.split(char)]
            )
    print(text, end="")
