from __future__ import annotations

class Point:
    """Model a 2-D point."""

    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initialize a point with its x,y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float):
        """Mutates a point object as it modifies Point's x and y attributes."""
        self.x += factor
        self.y += factor

    def scale(self, factor: float) -> Point:
        """Does not mutate Point object, but creates and returns a new point."""
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled
    
    def __str__(self):
        """Print prettier version of point."""
        return f"({self.x}, {self.y})"
    
    def __mul__(self, factor: float) -> Point:
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled
    
    def __getitem__(self, index: int) -> float:
        """Overloading subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError
        
    def __add__(self, rhs: float) -> Point:
        new_x: float = self.x + rhs
        new_y: float = self.y + rhs
        added_point: Point = Point(new_x, new_y)
        return added_point

#for LS 26   
a: Point = Point (1.0, 2.0)
b: Point = a.scale(3.0)

print(str(a))
print(b)
print(f"My point is: {b}")


#for LS 27
#a: Point = Point(1.0, 2.0)
#b: Point = a * 3.0
#print(b[3]) y-coord