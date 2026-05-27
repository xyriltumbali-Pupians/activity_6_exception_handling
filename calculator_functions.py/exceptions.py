class CalculatorError(Exception):
    pass


class DivisionByZeroError(CalculatorError):
    pass


class InvalidInputError(CalculatorError):
    pass