#!/usr/bin/python3

"""A function that retrive an element from a list."""


def element_at(my_list, idx):
    list_len = len(my_list)

    if idx < 0 or idx >= list_len:
        return None
    return my_list[idx]
