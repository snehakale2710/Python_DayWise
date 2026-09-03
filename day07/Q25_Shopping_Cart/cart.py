cart = []


def add_product(name, price):

    product = {
        "name": name,
        "price": price
    }

    cart.append(product)

    print("Product added.")


def remove_product(name):

    for product in cart:

        if product["name"] == name:

            cart.remove(product)

            print("Product removed.")

            return

    print("Product not found.")


def calculate_total():

    total = 0

    for product in cart:

        total += product["price"]

    return total


def display_cart():

    if not cart:

        print("Cart is empty.")

        return

    print("\n--- Cart ---")

    for product in cart:

        print(
            product["name"],
            "- ₹",
            product["price"]
        )

    print("Total =", calculate_total())