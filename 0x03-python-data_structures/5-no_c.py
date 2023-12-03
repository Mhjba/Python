#!/usr/bin/python3
def no_c(my_string):
    string_char = list(my_string)
    for char in string_char:
        if char == 'c' or char == 'C':
            string_char.remove(char)
    return("".join(string_char))
