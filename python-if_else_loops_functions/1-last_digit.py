#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    nb = number % -10
else:
    nb = number % 10
if nb > 5:
    print(f"Last digit of {number} is {nb} and is greater than 5")
elif nb == 0:
    print(f"Last digit of {number} is {nb} and is 0")
else:
    print(f"Last digit of {number} is {nb} and is less than 6 and not 0")
