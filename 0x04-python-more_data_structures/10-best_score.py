#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        my_key = max(a_dictionary, key=a_dictionary.get)
    else:
        my_key = None
    return (my_key)
