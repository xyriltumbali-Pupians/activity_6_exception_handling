from operations import Operations  # IMPORT child class

def main():
    calc = Operations()

    while True:
        choice = calc.choose_operation()
        num1, num2 = calc.get_numbers()

        if num1 is None or num2 is None:
            continue

        if choice == '1':
            result = calc.add(num1, num2)
        elif choice == '2':
            result = calc.subtract(num1, num2)
        elif choice == '3':
            result = calc.multiply(num1, num2)
        elif choice == '4':
            result = calc.divide(num1, num2)
        else:
            print("Invalid choice!")
            continue

        if result is not None:
            print("Result:", result)

        again = input("\nTry again? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you!")
            break


if __name__ == "__main__":
    main()