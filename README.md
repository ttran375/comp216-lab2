# Lab Exercises - Lectures 1 - 4

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ttran375/comp216-lab2/blob/main/src/main.ipynb)

## Lecture 1

### Question 1

Create a one-line expression that achieve the same output as
the below with the square bracket notation.

```python
NBA = dict(
    OklahomaCity="Thunder",
    Dallas="Mavericks",
    Boston="Celtics",
    NewYork="Knicks",
    Denver="Nuggets",
)

retrieve = NBA.get("Toronto", False)
print(retrieve)
```

### Question 2

Given two numbers, a and b, write a function called
compare_numbers that returns a string indicating the following:

- If a is greater than b, return "a is greater"

- If b is greater than a, return "b is greater"

- If both numbers are equal, return "a and b are equal"

Use the ternary operator to implement the function.

```python
def compare_numbers(a, b):
    pass
```

### Question 3: Examine following JS code snippet and re-create the logic

using Python. Implement the logic as a function that accepts secret_word
as a positional parameter and max_attempt as keyword parameter.

```js
let secret_word = "javascript";
let max_attempt = 5;
do {
    userInput = prompt("Enter the secret word: ");
    max_attempt -= 1;
    console.log(max_attempt)
} while (secret_word != userInput && max_attempt > 0);
```

### Question 4

Based on the following function definition, identify which
of the following parameters are positional-only, keyword-only and/or may
be positionally or by keyword.

```python
def processor(value_1, value_2, /, value_3, value_4=False, *, value_5, value_6):
    text = (value_1 + value_2).upper()
    if value_3:
        text += "!"
    if value_4:
        text = list(text)
        text.extend((value_5, value_6))
    return text
```

## Lecture 2

### Question 1

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

### Question 2

Based on the Triangle Class (above), create an Isosceles
Triangle Subclass (e.g., two side and two angles are equal). Override
and extend any inherited methods as needed.

- Create an Instance Method to determine the height of an isosceles
    triangle.

## Lecture 3

### Question 1

A user profile class was introduced into an application
based on the following definition:

```python
class User:
    registered_user_count = 0

    def __init__(self, first_name, last_name, age, postal_code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.postal_code = postal_code

    def registered(self, status):
        self.registered = status
        User.registered_user_count += 1
```

Update the relevant methods to ensure:

- The first_name and last_name attributes are supplied as strings that
    only contain alphabetical characters. If not, raise a Value Error.

- The age attribute is supplied as an integer and the age \> 13. If
    not, raise a Value Error.

- The postal_code attribute is supplied as that only contains
    alphanumerical characters. If not, raise a Value Error and
    auto-populate the attribute with the value: ‘X0X0X0’.

### Question 2

Use the following list of tuples that contains and scores of
students.

```python
students_scores = [
    ("Alice James", 85),
    ("Adam Bonson", 90),
    ("Matt Fowler", 78),
    ("David Curry", 92),
    ("Eva Porter", 80),
    ("Azure Kelsey", 79),
    ("Billie Jose", 64),
    ("Willian Maxime", 86),
]
```

Create a dictionary that includes high achieving (or honour) students
represented as key-value pairs:

- Keys must only include the first initial of the first name and full
    last name

- Values must only include scores that are 80% and higher

The expected output is the following:

```python
honour_students = {
    "A. James": 85,
    "A. Bonson": 90,
    "D. Curry": 92,
    "E. Porter": 80,
    "W. Maxime": 86,
}
```

### Question 3

Given the range object (below), create a single line
statement that utilizes a map(), filter() and lambda functions to
achieve the following:

- Filter the list to include only the even numbers.

- Square each of the filtered even numbers.

Use the following as the input: `numbers = range(1, 75, 3)`.

Afterwards, implement the same logic utilizing for loops and compare the
difference in the compute time between the two approaches.
