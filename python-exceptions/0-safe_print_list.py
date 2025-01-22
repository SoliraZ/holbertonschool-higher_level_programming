#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
        return (i + 1)
    except IndexError:
        print()
        return (i)
    except TypeError:
        print()
        return (i)
    return (i)
