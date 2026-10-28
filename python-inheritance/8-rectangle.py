#!/usr/bin/python3
"""Define a rectangle class that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with validated dimensions."""

    def __init__(self, width, height):
        """Initialize a rectangle with positive integer dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
