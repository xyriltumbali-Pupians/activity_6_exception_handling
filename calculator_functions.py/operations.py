from calculator import Calculator


class Operations(Calculator):
    """Extended calculator operations with error handling and validation."""

    def add(self, a, b):
        self._validate_numbers(a, b)
        return a + b

    def subtract(self, a, b):
        self._validate_numbers(a, b)
        return a - b

    def multiply(self, a, b):
        self._validate_numbers(a, b)
        return a * b

    def divide(self, a, b):
        self._validate_numbers(a, b)

        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")

        return a / b

    def power(self, a, b):
        self._validate_numbers(a, b)
        return a ** b

    def _validate_numbers(self, a, b):
        """Ensures inputs are valid numbers."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers (int or float)")