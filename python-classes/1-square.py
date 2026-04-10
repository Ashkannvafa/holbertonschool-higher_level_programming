#!/usr/bin/python3
"""This module defines a Square class with a private size attribute."""


class Square:
    """This class represents a square with a defined size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (any): The size of the square (no validation required).
        """
        self.__size = size
