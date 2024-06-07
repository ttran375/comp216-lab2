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

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not value.isalpha():
            raise ValueError(
                "First name must contain only alphabetical characters.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not value.isalpha():
            raise ValueError(
                "Last name must contain only alphabetical characters.")
        self._last_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 13:
            raise ValueError("Age must be an integer greater than 13.")
        self._age = value

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, value):
        if not value.isalnum():
            value = 'X0X0X0'
        self._postal_code = value


def main():
    try:
        # Valid User objects
        user1 = User("John", "Doe", 25, "12345")
        user2 = User("Jane", "Smith", 30, "A1B2C3")

        # Registering valid users
        user1.registered(True)
        user2.registered(True)

        # Printing User details
        print(f"User 1: {user1.first_name} {user1.last_name}, Age: {
              user1.age}, Postal Code: {user1.postal_code}, Registered: {user1.registered}")
        print(f"User 2: {user2.first_name} {user2.last_name}, Age: {
              user2.age}, Postal Code: {user2.postal_code}, Registered: {user2.registered}")

        # Printing the total number of registered users
        print(f"Total registered users: {User.registered_user_count}")

        # Invalid User objects
        try:
            User("Alice", "Johnson", 12, "L5N6P7")  # Invalid age
        except ValueError as e:
            print(f"Error: {e}")

        try:
            User("Alice123", "Johnson", 20,
                 "L5N6P7")  # Invalid first name
        except ValueError as e:
            print(f"Error: {e}")

        try:
            User("Alice", "Johnson456", 20,
                 "L5N6P7")  # Invalid last name
        except ValueError as e:
            print(f"Error: {e}")

        try:
            # Invalid postal code
            user6 = User("Alice", "Johnson", 20, "!@#$%^")
            print(user6)
        except ValueError as e:
            print(f"Error: {e}")

        # Test with default postal code due to invalid input
        user7 = User("Bob", "Brown", 20, "!@#$%^")
        print(f"User 7: {user7.first_name} {user7.last_name}, Age: {
              user7.age}, Postal Code: {user7.postal_code}")
        
        user7 = User("Bob", "Brown", 20, "!@#$%^")
        print(f"User 7: {user7.first_name} {user7.last_name}, Age: {
              user7.age}, Postal Code: {user7.postal_code}")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
