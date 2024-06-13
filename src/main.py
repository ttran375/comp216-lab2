import math


class Triangle:
    def __init__(self, sides, angles):
        self.sides = sides
        self.angles = angles

    @property
    def sides(self):
        return self._sides

    @sides.setter
    def sides(self, value):
        if len(value) != 3:
            raise ValueError("Exactly three side lengths must be provided.")
        if not all(isinstance(x, (int, float)) and x > 0 for x in value):
            raise ValueError(
                "All side lengths must be non-zero integers or floats.")
        self._sides = value

    @property
    def angles(self):
        return self._angles

    @angles.setter
    def angles(self, value):
        if len(value) != 3:
            raise ValueError("Exactly three angle values must be provided.")
        if not all(isinstance(x, (int, float)) and x > 0 for x in value):
            raise ValueError(
                "All angle values must be non-zero integers or floats.")
        if not math.isclose(sum(value), 180, rel_tol=1e-9):
            raise ValueError("The sum of the angles must be 180 degrees.")
        self._angles = value

    def perimeter(self):
        return sum(self.sides)

    @staticmethod
    def hypotenuse(side1, side2):
        if not (isinstance(side1, (int, float)) and isinstance(side2, (int, float))):
            raise ValueError("Both sides must be integers or floats.")
        return (side1 ** 2 + side2 ** 2) ** 0.5

    def __lt__(self, other):
        if not isinstance(other, Triangle):
            return NotImplemented
        return self.perimeter() < other.perimeter()

    def __iter__(self):
        return iter(self.sides)


class IsoscelesTriangle(Triangle):
    def __init__(self, sides, angles):
        super().__init__(sides, angles)
        if not (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]):
            raise ValueError(
                "In an isosceles triangle, at least two sides must be equal.")
        if not (angles[0] == angles[1] or angles[1] == angles[2] or angles[0] == angles[2]):
            raise ValueError(
                "In an isosceles triangle, at least two angles must be equal.")

    def height(self):
        if self.sides[0] == self.sides[1]:
            base = self.sides[2]
            equal_side = self.sides[0]
        elif self.sides[1] == self.sides[2]:
            base = self.sides[0]
            equal_side = self.sides[1]
        else:
            base = self.sides[1]
            equal_side = self.sides[0]

        height = math.sqrt(equal_side ** 2 - (base / 2) ** 2)
        return height


def main():

    triangle1 = Triangle([3, 4, 5], [90, 53.13, 36.87])
    triangle2 = Triangle([6, 8, 10], [90, 53.13, 36.87])
    isosceles_triangle = IsoscelesTriangle([5, 5, 3.42], [70, 70, 40])

    print("Perimeter of triangle1:", triangle1.perimeter())
    print("Perimeter of triangle2:", triangle2.perimeter())

    print("Hypotenuse of sides 3 and 4:",
          Triangle.hypotenuse(3, 4))

    print("Is triangle1 smaller than triangle2?",
          triangle1 < triangle2)

    print("Sides of triangle2:")
    for side in triangle2:
        print(side)

    print("Height of isosceles triangle:", isosceles_triangle.height())


if __name__ == "__main__":
    main()
