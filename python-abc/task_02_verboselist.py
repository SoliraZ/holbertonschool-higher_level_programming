#!/usr/bin/python3
""" Task 02: Verboselist """


class VerboseList(list):
    """ Verboselist class """
    def append(self, item):
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, nb_item):
        print(f"Extended the list with [{len(nb_item)}] items.")
        super().extend(nb_item)

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return (super().pop(index))
