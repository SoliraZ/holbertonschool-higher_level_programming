#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = list(my_list)
    for i in range(len(new_list)):
        if (new_list[i] % 2 == 0):
            new_list[i] = 1
        else:
            new_list[i] = 0
    return (new_list)
