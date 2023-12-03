#!/usr/bin/env python3
def no_c(my_string):
    my_string_char = list(my_string)
    for char in my_string_char:
        if char == 'c' or char == 'C':
            my_string_char.remove(char)
    return "".join(my_string_char)
