"""
Solution: Implements a hierarchy of geometric shapes with inheritance.

This solution defines three classes:
- Polygon: Base class for all shapes, calculates area using the shoelace formula
- Rectangle: Inherits from Polygon, represents a rectangle
- Square: Inherits from Rectangle, represents a square with a simplified area calculation
"""
class Polygon:
    """
    A class representing a polygon defined by its vertices.

    Attributes:
        points (list): A list of (x, y) coordinate pairs representing the vertices
        nb_of_vertices (int): The number of vertices in the polygon
    """
    def __init__(self, points):
        """
        Initialize a polygon with a list of points.

        Args:
            points (list): A list of (x, y) coordinate pairs representing the vertices
        """
        print('I am a polygon')
        self.points = points
        self.nb_of_vertices = len(points)

    def area(self):
        """
        Calculate the area of the polygon using the shoelace formula.

        The shoelace formula is a mathematical algorithm to determine the area of a
        simple polygon whose vertices are described by their Cartesian coordinates.

        Returns:
            float: The area of the polygon
        """
        print('Computed using the shoelace formula')
        # 1. Separate x and y coordinates
        x, y = list(zip(*self.points))
        n = self.nb_of_vertices

        # 2. First sum: sum x[i] * y[j], where j is the next vertex
        sum1 = 0
        for i in range(n):
            j = (i + 1) % n      # next index, wrap around to 0
            sum1 += x[i] * y[j]

        # 3. Second sum: sum y[i] * x[j]
        sum2 = 0
        for i in range(n):
            j = (i + 1) % n
            sum2 += y[i] * x[j]

        # 4. Shoelace formula: |sum1 - sum2| / 2
        area = abs(sum1 - sum2) / 2
        return area

class Rectangle(Polygon):
    """
    A class representing a rectangle, which is a special type of polygon.

    Inherits from Polygon and uses its area calculation method.
    """
    def __init__(self, points):
        """
        Initialize a rectangle with a list of points.

        Args:
            points (list): A list of (x, y) coordinate pairs representing the vertices
        """
        super().__init__(points)
        print('More precisely, I am a rectangle')

    def area(self):
        """
        Calculate the area of the rectangle using the parent's method.

        Returns:
            float: The area of the rectangle
        """
        print('I could compute it more easily, but well, I leave it to Polygon...')
        return super().area()


class Square(Rectangle):
    """
    A class representing a square, which is a special type of rectangle.

    Inherits from Rectangle but overrides the area calculation method.
    """
    def __init__(self, points):
        """
        Initialize a square with a list of points.

        Args:
            points (list): A list of (x, y) coordinate pairs representing the vertices
        """
        super().__init__(points)
        print('Even more precisely, I am a square')

    def area(self):
        """
        Calculate the area of the square as side_length^2.

        Returns:
            float: The area of the square
        """
        print('I compute it myself!')
        return max(abs(self.points[0][0] - self.points[1][0]),
                    abs(self.points[0][1] - self.points[1][1])
                    ) ** 2