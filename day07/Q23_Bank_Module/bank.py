balance = 0


def deposit(amount):

    global balance

    balance += amount

    print("Amount deposited successfully.")


def withdraw(amount):

    global balance

    if amount <= balance:

        balance -= amount

        print("Amount withdrawn successfully.")

    else:

        print("Insufficient balance.")


def check_balance():

    return balance