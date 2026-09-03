# 1. Function to print Hello Python
def hello():
    print("Hello Python")


# 2. Function that accepts a name
def greet(name):
    print("Hello", name)


# 3. Function to add two numbers
def add(a, b):
    return a + b


# 4. Functions for arithmetic operations
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


# 5. Function to check even/odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# 6. Function to check positive/negative/zero
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


# 7. Function to calculate factorial
def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact


# 8. Function to find largest of two numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b


# 9. Function to calculate student percentage
def percentage(marks):
    total = sum(marks)
    return total / len(marks)


# 10. Function that accepts a list and returns its sum
def list_sum(numbers):
    return sum(numbers)


# ==========================
# FUNCTION CALLS
# ==========================

hello()

greet("Sneha")

print("Sum of two numbers =", add(10, 20))

print("Addition =", addition(20, 10))
print("Subtraction =", subtraction(20, 10))
print("Multiplication =", multiplication(20, 10))
print("Division =", division(20, 10))

print("7 is", check_even_odd(7))

print("-5 is", check_number(-5))

print("Factorial of 5 =", factorial(5))

print("Largest =", largest(25, 40))

marks = [80, 75, 90, 85, 70]
print("Student Percentage =", percentage(marks), "%")

numbers = [10, 20, 30, 40, 50]
print("List Sum =", list_sum(numbers))