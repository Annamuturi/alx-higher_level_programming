#!/usr/bin/python3

def no_c(my_string):
    final_str = ''
    for char in my_string:
        if my_string != 'c' and my_string != 'C':
            final_str += my_string
        return (final_str)
