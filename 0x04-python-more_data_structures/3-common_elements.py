#!/usr/bin/python3
def common_elements(set_1, set_2):
    return [common_elements for common_elements in set_1
            if common_elements in set_2]
