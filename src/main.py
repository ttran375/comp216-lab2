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
            raise ValueError("There must be exactly 3 side lengths.")
        if not all(isinstance(side, (int, float)) and side > 0 for side in value):
            raise ValueError(
                "All side lengths must be positive non-zero numbers.")
        self._sides = value

    @property
    def angles(self):
        return self._angles

    @angles.setter
    def angles(self, value):
        if len(value) != 3:
            raise ValueError("There must be exactly 3 angles.")
        if not all(isinstance(angle, (int, float)) and angle > 0 for angle in value):
            raise ValueError("All angles must be positive non-zero numbers.")
        if sum(value) != 180:
            raise ValueError("The angles must add up to 180 degrees.")
        self._angles = value

    def calculate_perimeter(self):
        return sum(self.sides)

    @staticmethod
    def calculate_hypotenuse(side1, side2):
        return (side1 ** 2 + side2 ** 2) ** 0.5

    def __gt__(self, other):
        if not isinstance(other, Triangle):
            return NotImplemented
        return self.calculate_perimeter() > other.calculate_perimeter()

    def __iter__(self):
        return iter(self.sides)


class IsoscelesTriangle(Triangle):
    def __init__(self, sides, angles):
        super().__init__(sides, angles)
        if len(set(sides)) != 2 or len(set(angles)) != 2:
            raise ValueError(
                "For an isosceles triangle, there must be two equal sides and two equal angles.")

    def calculate_height(self):
        base = self.sides[0] if self.sides[1] == self.sides[2] else self.sides[2]
        equal_side = self.sides[1] if self.sides[1] == self.sides[2] else self.sides[0]
        height = (equal_side ** 2 - (base / 2) ** 2) ** 0.5
        return height


def main():
    try:
        triangle = Triangle([3, 4, 5], [90, 60, 30])
        print(f"Triangle perimeter: {
              triangle.calculate_perimeter()}")

        print(f"Hypotenuse: {Triangle.calculate_hypotenuse(3, 4)}")
        print(f"Triangle sides: {list(triangle)}")

        triangle2 = Triangle([6, 8, 10], [90, 60, 30])
        print(f"Is triangle1 > triangle2? {
              triangle > triangle2}")

        isosceles_triangle = IsoscelesTriangle([5, 5, 8], [70, 70, 40])
        print(f"IsoscelesTriangle perimeter: {
              isosceles_triangle.calculate_perimeter()}")

        print(f"IsoscelesTriangle height: {
              isosceles_triangle.calculate_height()}")
        print(f"IsoscelesTriangle sides: {
              list(isosceles_triangle)}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
