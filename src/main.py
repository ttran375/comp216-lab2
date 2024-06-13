class Triangle:
    def __init__(self, sides, angles):
        if len(sides) != 3 or len(angles) != 3:
            raise ValueError(
                "There must be exactly 3 side lengths and 3 angle values.")
        if not all(isinstance(value, (int, float)) and value > 0 for value in sides + angles):
            raise ValueError("All values must be non-zero integers or floats.")
        if sum(angles) != 180:
            raise ValueError("The angles must add up to 180 degrees.")

        self.sides = sides
        self.angles = angles

    @property
    def sides(self):
        return self._sides

    @sides.setter
    def sides(self, value):
        if len(value) != 3:
            raise ValueError("There must be exactly 3 side lengths.")
        if not all(isinstance(val, (int, float)) and val > 0 for val in value):
            raise ValueError(
                "All side lengths must be non-zero integers or floats.")
        self._sides = value

    @property
    def angles(self):
        return self._angles

    @angles.setter
    def angles(self, value):
        if len(value) != 3:
            raise ValueError("There must be exactly 3 angle values.")
        if not all(isinstance(val, (int, float)) and val > 0 for val in value):
            raise ValueError(
                "All angle values must be non-zero integers or floats.")
        if sum(value) != 180:
            raise ValueError("The angles must add up to 180 degrees.")
        self._angles = value

    def perimeter(self):
        return sum(self.sides)

    @staticmethod
    def hypothenuse(side1, side2):
        if not all(isinstance(val, (int, float)) and val > 0 for val in [side1, side2]):
            raise ValueError("The sides must be non-zero integers or floats.")
        return (side1**2 + side2**2)**0.5

    def __gt__(self, other):
        if not isinstance(other, Triangle):
            return NotImplemented
        return self.perimeter() > other.perimeter()

    def __iter__(self):
        return iter(self.sides)


# Example Usage
triangle1 = Triangle([3, 4, 5], [90, 60, 30])
triangle2 = Triangle([6, 8, 10], [90, 45, 45])

print("Perimeter of triangle1:", triangle1.perimeter())
print("Hypothenuse of sides 3 and 4:", Triangle.hypothenuse(3, 4))

# Comparison based on perimeter
print("Triangle1 is larger than Triangle2:", triangle1 > triangle2)

# Iterating over side lengths
for side in triangle1:
    print("Side length:", side)
