from operations import Addition, Subtraction, Multiplication, Division
from exceptions import InvalidInputError, CalculatorError


class CalculatorApp:
    def __init__(self):
        self.history = []
        self.last_result = None

    def display_menu(self):
        print("\n==== CALCULATOR APP ====")
        print("[1] Add")
        print("[2] Subtract")
        print("[3] Multiply")
        print("[4] Divide")
        print("[5] View History")
        print("[0] Exit")