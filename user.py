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
