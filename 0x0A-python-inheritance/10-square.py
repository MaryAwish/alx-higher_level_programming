#!/usr/bin/python3
"""
Contains class BaseGeometry, subclass Rectangle and subclass square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size):
        """Instatiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returnsthe area of the square"""
        return self.__size ** 2
