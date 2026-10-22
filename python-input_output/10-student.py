#!/usr/bin/python3
"""Student class with filtering features."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the student dictionary representation."""
        if isinstance(attrs, list) and all(
            isinstance(s, str) for s in attrs
        ):
            res = {}
            for a in attrs:
                if hasattr(self, a):
                    res[a] = getattr(self, a)
            return res
        return self.__dict__
