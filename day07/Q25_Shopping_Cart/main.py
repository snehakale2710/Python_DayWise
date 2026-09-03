import cart


while True:

    print("\n--- Shopping Cart ---")

    print("1. Add Product")
    print("2. Remove Product")
    print("3. Display Cart")
    print("4. Calculate Total")
    print("5. Exit")

    choice = input("Enter choice: ")


    if choice == "1":

        name = input("Enter product name: ")

        price = float(input("Enter product price: "))

        cart.add_product(name, price)


    elif choice == "2":

        name = input("Enter product name: ")

        cart.remove_product(name)


    elif choice == "3":

        cart.display_cart()


    elif choice == "4":

        print(
            "Total =",
            cart.calculate_total()
        )


    elif choice == "5":

        print("Thank you!")

        break


    else:

        print("Invalid choice.")