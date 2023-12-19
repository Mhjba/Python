#!/usr/bin/python3
"""Square module """


class Square():
    """Defines a square."""

    def __init__(self, size=0):
        """constructor.

        Args:
            size : length of a side of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2i
