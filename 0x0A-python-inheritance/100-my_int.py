#!/usr/bin/python3
"""MyInt class module"""


class MyInt(int):
    """MyInt class inherits from int"""
    def __eq__(self, other_int):
        """inverted =="""
        if self is not other_int:
            return False
        return True

    def __ne__(self, other_int):
        """inverted !="""
        if self is other_int:
            return False
        return True
