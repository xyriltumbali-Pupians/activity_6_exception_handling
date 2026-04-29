class Calculator:
    def get_numbers(self):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            return None, None

    def choose_operation(self):
        print("\nChoose operation:")
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")

        return input(f"Enter choice (1/2/3/4): ")