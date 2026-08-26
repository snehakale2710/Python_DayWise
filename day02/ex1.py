# 1. DATA TYPES
age = 22                 
height = 5.9            
name = "Sneha"          
is_student = True        

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

# 2. INPUT
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print("Name:", name)
print("Age:", age)
print("Height:", height)

# 3. ARITHMETIC OPERATORS
num1 = 15
num2 = 4

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Remainder:", num1 % num2)
print("Power:", num1 ** 2)

# 4. COMPARISON OPERATORS
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# 5. LOGICAL OPERATORS
age = 22

print(age > 18 and age < 30)
print(age < 18 or age > 20)
print(not age > 18)


# 6. IF-ELSE
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# 7. IF-ELIF-ELSE
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Fail")

# 8. PRACTICAL TASK 1: EVEN OR ODD
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 9. PRACTICAL TASK 2: MAXIMUM OF TWO NUMBERS
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Maximum number:", num1)
elif num2 > num1:
    print("Maximum number:", num2)
else:
    print("Both numbers are equal")

# 10. NESTED IF
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")

    if age >= 21:
        print("You are above 21")
else:
    print("You are a minor")