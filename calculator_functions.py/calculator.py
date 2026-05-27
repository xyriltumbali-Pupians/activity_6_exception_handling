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
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            raise InvalidInputError("Invalid input! Please enter numbers only.")

    def perform_operation(self, choice, num1, num2):
        operations = {
            "1": Addition(),
            "2": Subtraction(),
            "3": Multiplication(),
            "4": Division()
        }

        operation = operations.get(choice)
        if not operation:
            raise InvalidInputError("Invalid operation selected!")

        return operation.calculate(num1, num2)

    def save_history(self, num1, num2, choice, result):
        symbols = {"1": "+", "2": "-", "3": "*", "4": "/"}
        self.history.append(f"{num1} {symbols.get(choice)} {num2} = {result}")

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
                num1, num2 = self.get_numbers()
                result = self.perform_operation(choice, num1, num2)

                print(f"Result: {result}")
                self.save_history(num1, num2, choice, result)
                self.last_result = result

            except CalculatorError as e:
                print(f"Error: {e}")