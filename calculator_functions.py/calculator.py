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

        operation = operations.get(choice)
        if not operation:
            raise InvalidInputError("Invalid operation selected!")

        return operation.calculate(a, b)

    def save_history(self, a, b, choice, result):
        symbols = {"1": "+", "2": "-", "3": "*", "4": "/"}
        self.history.append(f"{a} {symbols.get(choice)} {b} = {result}")

    def show_history(self):
        if not self.history:
            print("No history yet.")
        else:
            for i, record in enumerate(self.history, 1):
                print(f"{i}. {record}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option: ")

            if choice == "0":
                print("Thank you!\U0001F431 MEOW")
                break

            if choice == "5":
                self.show_history()
                continue

            try:
                a, b = self.get_numbers()
                result = self.perform_operation(choice, a, b)

                print(f"Result: {result}")
                self.save_history(a, b, choice, result)
                self.last_result = result

            except CalculatorError as e:
                print(f"Error: {e}")