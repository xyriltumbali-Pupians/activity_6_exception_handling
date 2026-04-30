class Calculator:
    def get_numbers(self):
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                return num1, num2
            except ValueError:
                print("Invalid input! Please enter numbers only.\n")

    def choose_operation(self):
        operations = {
            "1": "Addition",
            "2": "Subtraction",
            "3": "Multiplication",
            "4": "Division"
        }

        print("\nChoose operation:")
        for key, value in operations.items():
            print(f"{key} - {value}")

        while True:
            choice = input("Enter choice (1/2/3/4): ")
            if choice in operations:
                return choice
            print("Invalid choice! Please select 1, 2, 3, or 4.\n")