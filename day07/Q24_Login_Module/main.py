import authentication


while True:

    print("\n--- Login System ---")

    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")


    if choice == "1":

        username = input("Enter username: ")

        password = input("Enter password: ")

        print(
            authentication.register_user(
                username,
                password
            )
        )


    elif choice == "2":

        username = input("Enter username: ")

        password = input("Enter password: ")

        print(
            authentication.login_user(
                username,
                password
            )
        )


    elif choice == "3":

        print("Goodbye!")

        break


    else:

        print("Invalid choice.")