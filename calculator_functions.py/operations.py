from exceptions import DivisionByZeroError

class Operation:
    def calculate(self, a, b):
        raise NotImplementedError


class Addition(Operation):
    def calculate(self, a, b):
        return a + b


class Subtraction(Operation):
    def calculate(self, a, b):
        return a - b


class Multiplication(Operation):
    def calculate(self, a, b):
        return a * b


class Division(Operation):
    def calculate(self, a, b):
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero!")
        return a / b