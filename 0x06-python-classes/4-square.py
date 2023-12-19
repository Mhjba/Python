#!/usr/bin/python3
"""Square module"""


class Square:
    """Class square .

    Args:
        size : length of a side of the square
"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """__size getter, setter with same method name

        Returns:
            __size (int): length of one side, squared

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Args"""


        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calulates area of square"""


        area = self.__size * self.__size
        return area
