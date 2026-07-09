#!/usr/bin/env python3
"""Module demonstrating mixins."""


class SwimMixin:
    """Mixin that provides swimming behavior."""

    def swim(self):
        """Print the swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying behavior."""

    def fly(self):
        """Print the flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon."""

    def roar(self):
        """Print the dragon's roar."""
        print("The dragon roars!")
