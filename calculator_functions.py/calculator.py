class Calculator:
    def __init__(self):
        self.operations = {
            "1": ("Addition", lambda a, b: a + b),
            "2": ("Subtraction", lambda a, b: a - b),
            "3": ("Multiplication", lambda a, b: a * b),
            "4": ("Division", self.safe_divide)
        }

    def get_numbers(self):
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
               