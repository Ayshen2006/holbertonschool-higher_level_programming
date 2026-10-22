#!/usr/bin/env python3
"""Define abstract shapes and calculate their properties."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the shape's area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the shape's perimeter."""
        pass


class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius):
        """Initialize a circle with a radius."""
        self.radius = radius

    def area(self):
        """Return the circle's area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the circle's perimeter."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the rectangle's area."""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle's perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
