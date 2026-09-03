import calculator

while True:

    print("\n--- Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "5":
        print("Calculator closed.")
        break

    if choice in ["1", "2", "3", "4"]:

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result =", calculator.add(a, b))

        elif choice == "2":
            print("Result =", calculator.subtract(a, b))

        elif choice == "3":
            print("Result =", calculator.multiply(a, b))

        elif choice == "4":
            print("Result =", calculator.divide(a, b))

    else:
        print("Invalid choice.")