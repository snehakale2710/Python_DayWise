import number_utils


n = int(input("Enter a number: "))


print(
    "Even:",
    number_utils.is_even(n)
)


print(
    "Prime:",
    number_utils.is_prime(n)
)


print(
    "Factorial:",
    number_utils.factorial(n)
)


print(
    "Reverse:",
    number_utils.reverse_number(n)
)