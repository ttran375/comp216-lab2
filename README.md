# Lecture 2

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ttran375/comp216-lab2/blob/main/src/main.ipynb)

## Question 1

Create a Triangle Class based on the following
specifications:

- Two arguments are accepted: 1) List of side lengths; 2) List of angles.

  - Validate 3 side length values and 3 angle values are provided.

  - All values in the list must be non-zero Int or Float.

  - The angles must add up to 180°

  - Hint: Use Property or Descriptor-based attributes.

- Create an Instance method to calculate the perimeter of the
    triangle.

- Create a Static method to calculate the hypothenuse when supplied
    with two sides.

- Create a Dunder method to determine if one triangle instance is
    larger than another based it perimeter.

- Create a Dunder method to generate an iterator based on the side
    lengths of a specific instance.

## Question 2

Based on the Triangle Class (above), create an Isosceles
Triangle Subclass (e.g., two side and two angles are equal). Override
and extend any inherited methods as needed.

- Create an Instance Method to determine the height of an isosceles
    triangle.
