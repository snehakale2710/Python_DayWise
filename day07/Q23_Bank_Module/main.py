import bank


while True:

    print("\n--- Bank Menu ---")

    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter choice: ")


    if choice == "1":

        amount = float(input("Enter amount: "))

        bank.deposit(amount)


    elif choice == "2":

        amount = float(input("Enter amount: "))

        bank.withdraw(amount)


    elif choice == "3":

        print("Balance =", bank.check_balance())


    elif choice == "4":

        print("Thank you!")

        break


    else:

        print("Invalid choice.")