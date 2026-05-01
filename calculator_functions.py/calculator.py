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
        
    def get_numbers(self):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            raise InvalidInputError("Invalid input! Please enter numbers only.")

    def perform_operation(self, choice, a, b):
        operations = {
            "1": Addition(),
            "2": Subtraction(),
            "3": Multiplication(),
            "4": Division()
        }