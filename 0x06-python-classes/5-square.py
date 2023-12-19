#!/usr/bin/python3
"""Square module"""


class Square:
    """Class defined"""


    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """__size getter"""


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

    def my_print(self):
        """Prints text representation of square in hash chars"""


        for row in range(0, self.__size):
            for col in range(0, self.__size):
                print("#", end="")
            print()
        if self.__size is 0:
            print()
