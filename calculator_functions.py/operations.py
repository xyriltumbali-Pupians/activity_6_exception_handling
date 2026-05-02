from exceptions import DivisionByZeroError

class Operation:
    def calculate(self, num1, num2):
        raise NotImplementedError


class Addition(Operation):
    def calculate(self, num1, num2):
        return num1 + num2


class Subtraction(Operation):
    def calculate(self, num1, num2):
        return num1 - num2


class Multiplication(Operation):
    def calculate(self, num1, num2):
        return num1 * num2


class Division(Operation):
    def calculate(self, num1, num2):
        if num2 == 0:
            raise DivisionByZeroError("Cannot divide by zero!")
        return num1 / num2