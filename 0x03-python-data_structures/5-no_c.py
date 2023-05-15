#!/usr/bin/python3

def no_c(my_string):
    final_str = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            final_str += char
        return (final_str)
