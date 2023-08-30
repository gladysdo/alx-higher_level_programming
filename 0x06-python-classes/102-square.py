#!/usr/bin/python3
class Square:
    """Define a square by its size and provide comparisons based on area."""

    def __init__(self, size=0):
        """Initialize the square with a given size."""
        self.size = size  # Using the property setter

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare two squares for equality based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare two squares for inequality based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare two squares for less than based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare two squares for less than or equal based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare two squares for greater than based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare two squares for greater than or equal based on area."""
        return self.area() >= other.area()
