#!/usr/bin/python3
"""Module that defines a Square class with area method."""


class Square:
    """A class that defines a square with validated size and area method."""

    def __init__(self, size=0):
        """Initialize Square with optional validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
