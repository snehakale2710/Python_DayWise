# 1. Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)


# 2. Print numbers from 1 to 100.
for i in range(1, 101):
    print(i)


# 3. Print all even numbers between 1 and 50.
for i in range(2, 51, 2):
    print(i)


# 4. Print all odd numbers between 1 and 50.
for i in range(1, 51, 2):
    print(i)


# 5. Print numbers from 10 to 1 in reverse order.
for i in range(10, 0, -1):
    print(i)


# 6. Print the multiplication table of a number entered by the user.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# 7. Find the sum of numbers from 1 to 100.
total = 0
for i in range(1, 101):
    total += i
print(total)


# 8. Find the sum of all even numbers from 1 to 100.
total = 0
for i in range(2, 101, 2):
    total += i
print(total)


# 9. Find the factorial of a number using a loop.
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(factorial)


# 10. Count how many numbers are present between 1 and a user-entered number.
num = int(input("Enter a number: "))
count = 0
for i in range(1, num + 1):
    count += 1
print(count)


# 11. Print numbers divisible by 5 between 1 and 100.
for i in range(1, 101):
    if i % 5 == 0:
        print(i)


# 12. Use a while loop to print numbers from 1 to 20.
i = 1
while i <= 20:
    print(i)
    i += 1


# 13. Use a while loop to print even numbers from 2 to 20.
i = 2
while i <= 20:
    print(i)
    i += 2


# 14. Create a program that keeps printing numbers and stops when the number becomes 5 using break.
for i in range(1, 11):
    if i == 5:
        break
    print(i)


# 15. Print numbers from 1 to 10 but skip 5 using continue.
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# 16. Create a program to find the sum of the first N natural numbers.
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total += i
print(total)


# 17. Create a program to calculate the power of a number without using the ** operator.
base = int(input("Enter base: "))
power = int(input("Enter power: "))
result = 1
for i in range(power):
    result *= base
print(result)


# 18. Print the first 10 multiples of 3.
for i in range(1, 11):
    print(3 * i)


# 19. Check how many numbers between 1 and 100 are divisible by both 2 and 5.
count = 0
for i in range(1, 101):
    if i % 2 == 0 and i % 5 == 0:
        count += 1
print(count)


# 20. Create a simple menu loop that repeats until the user enters 0.
while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("0. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 0:
        break

    if choice in [1, 2, 3]:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == 1:
            print(a + b)
        elif choice == 2:
            print(a - b)
        elif choice == 3:
            print(a * b)
    else:
        print("Invalid choice")