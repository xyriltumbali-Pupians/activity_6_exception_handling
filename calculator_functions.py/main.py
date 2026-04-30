from operations import Operations


def main():
    calc = Operations()

    while True:
        try:
            choice = calc.choose_operation()
            num1, num2 = calc.get_numbers()

            name, result = calc.calculate(choice, num1, num2)

            print(f"\n{name} result: {result}")

        except ValueError as e:
            print(f"\nError: {e}")

        again = input("\nTry again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Thank you!")
            break


if __name__ == "__main__":
    main()