# A. `__init__()` – Constructor
### Q1. Create a Student class with name, age, and course. Initialize the values using `__init__()` and display them.
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
student = Student("Sneha", 21, "MCA")
student.display()

### Q2. Create an Employee class with name, salary, and department. Use a constructor to initialize and display the data.
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)
employee = Employee("Rahul", 35000, "IT")
employee.display()

### Q3. Create a Book class with title, author, and price. Create 3 objects using `__init__()`.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def display(self):
        print(self.title, "-", self.author, "-", self.price)
book1 = Book("Python Basics", "John", 500)
book2 = Book("Java Programming", "Robert", 600)
book3 = Book("Web Development", "David", 700)
book1.display()
book2.display()
book3.display()

### Q4. Create a BankAccount class with account_no, holder_name, and balance. Initialize the account using a constructor.
class BankAccount:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance
    def display(self):
        print("Account No:", self.account_no)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)
account = BankAccount(101, "Sneha", 10000)
account.display()

# B. `__str__()` – Readable Object Representation
### Q5. Create a Student class and use `__str__()` to display student information in a readable format.
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    def __str__(self):
        return "Name: " + self.name + ", Age: " + str(self.age) + ", Course: " + self.course
student = Student("Sneha", 21, "MCA")
print(student)

### Q6. Create an Employee class with id, name, and salary. Override `__str__()` to display employee details.
class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    def __str__(self):
        return "Employee ID: " + str(self.id) + "\nName: " + self.name + "\nSalary: " + str(self.salary)
employee = Employee(101, "Rahul", 35000)
print(employee)

### Q7. Create a Hospital class with patient ID, patient name, and disease. Use `__str__()` to display patient details.
class Hospital:
    def __init__(self, patient_id, patient_name, disease):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.disease = disease
    def __str__(self):
        return "Patient ID: " + str(self.patient_id) + "\nPatient Name: " + self.patient_name + "\nDisease: " + self.disease
patient = Hospital(101, "Amit", "Fever")
print(patient)

# C. `@classmethod`
### Q8. Create a Student class with a class variable `school_name`. Create a class method to change the school name.
class Student:
    school_name = "ABC School"
    @classmethod
    def change_school(cls, name):
        cls.school_name = name
print(Student.school_name)
Student.change_school("XYZ School")
print(Student.school_name)

### Q9. Create an Employee class with a class variable `company_name`. Use `@classmethod` to update the company name.
class Employee:
    company_name = "ABC Company"
    @classmethod
    def change_company(cls, name):
        cls.company_name = name
print(Employee.company_name)
Employee.change_company("XYZ Company")
print(Employee.company_name)

### Q10. Create a Bank class with a class variable `bank_name`. Create a class method to change the bank name.
class Bank:
    bank_name = "State Bank"
    @classmethod
    def change_bank(cls, name):
        cls.bank_name = name
print(Bank.bank_name)
Bank.change_bank("National Bank")
print(Bank.bank_name)

### Q11. Create a Company class with company_name and location as class variables. Create a class method to update the location.
class Company:
    company_name = "ABC Company"
    location = "Pune"
    @classmethod
    def change_location(cls, location):
        cls.location = location
print(Company.company_name)
print(Company.location)
Company.change_location("Mumbai")
print(Company.location)

# D. `@staticmethod`
### Q12. Create a Calculator class with static methods for addition, subtraction, multiplication, and division.
class Calculator:
    @staticmethod
    def addition(a, b):
        return a + b
    @staticmethod
    def subtraction(a, b):
        return a - b
    @staticmethod
    def multiplication(a, b):
        return a * b
    @staticmethod
    def division(a, b):
        return a / b
print("Addition:", Calculator.addition(10, 5))
print("Subtraction:", Calculator.subtraction(10, 5))
print("Multiplication:", Calculator.multiplication(10, 5))
print("Division:", Calculator.division(10, 5))

### Q13. Create a MathUtility class with a static method to check whether a number is even or odd.
class MathUtility:
    @staticmethod
    def check_even_odd(number):
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")
MathUtility.check_even_odd(10)
MathUtility.check_even_odd(7)

### Q14. Create a Validator class with a static method to check whether an email contains `@`.
class Validator:
    @staticmethod
    def check_email(email):
        if "@" in email:
            print("Valid Email")
        else:
            print("Invalid Email")
Validator.check_email("sneha@gmail.com")
Validator.check_email("sneha.com")

### Q15. Create a PasswordValidator class with a static method to check whether a password has at least 8 characters.
class PasswordValidator:
    @staticmethod
    def check_password(password):
        if len(password) >= 8:
            print("Valid Password")
        else:
            print("Password must have at least 8 characters")
PasswordValidator.check_password("python123")
PasswordValidator.check_password("python")

### Q16. Create a Calculator class with a static method to calculate the square and cube of a number.
class Calculator:
    @staticmethod
    def square(number):
        return number * number
    @staticmethod
    def cube(number):
        return number * number * number
print("Square:", Calculator.square(5))
print("Cube:", Calculator.cube(5))

### Q17. Create an AgeValidator class with a static method to check whether a person is eligible to vote.
class AgeValidator:
    @staticmethod
    def check_age(age):
        if age >= 18:
            print("Eligible to vote")
        else:
            print("Not eligible to vote")
AgeValidator.check_age(21)
AgeValidator.check_age(16)

### Q18. Create a NumberUtility class with static methods to find factorial and sum of digits.
class NumberUtility:
    @staticmethod
    def factorial(number):
        result = 1
        for i in range(1, number + 1):
            result = result * i
        return result
    @staticmethod
    def sum_digits(number):
        total = 0
        while number > 0:
            total = total + number % 10
            number = number // 10
        return total
print("Factorial:", NumberUtility.factorial(5))
print("Sum of digits:", NumberUtility.sum_digits(1234))

### Q19. Create a StringUtility class with static methods to reverse a string and check whether it is a palindrome.
class StringUtility:
    @staticmethod
    def reverse_string(text):
        return text[::-1]
    @staticmethod
    def check_palindrome(text):
        if text == text[::-1]:
            return True
        else:
            return False
print("Reverse:", StringUtility.reverse_string("Python"))
print("Palindrome:", StringUtility.check_palindrome("madam"))

# E. `@property`
### Q20. Create a Student class with a private variable `_name`. Use `@property` to get the student's name.
class Student:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
student = Student("Sneha")
print(student.name)

### Q21. Create a Person class with `_age`. Use `@property` to get the age.
class Person:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
person = Person(21)
print(person.age)

### Q22. Create an Employee class with `_salary`. Use `@property` to display the salary.
class Employee:
    def __init__(self, salary):
        self._salary = salary
    @property
    def salary(self):
        return self._salary
employee = Employee(35000)
print(employee.salary)

### Q23. Create a Mobile class with `_brand` and use `@property` to access the brand.
class Mobile:
    def __init__(self, brand):
        self._brand = brand
    @property
    def brand(self):
        return self._brand
mobile = Mobile("Samsung")
print(mobile.brand)

### Q24. Create a Laptop class with `_ram`. Use `@property` to display RAM.
class Laptop:
    def __init__(self, ram):
        self._ram = ram
    @property
    def ram(self):
        return self._ram
laptop = Laptop(16)
print(laptop.ram, "GB")

### Q25. Create a Rectangle class with `_length` and `_width`. Use properties to access both values.
class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    @property
    def length(self):
        return self._length
    @property
    def width(self):
        return self._width
rectangle = Rectangle(10, 5)
print("Length:", rectangle.length)
print("Width:", rectangle.width)

# `@property` + Setter
### Q26. Create a Student class with `_marks`. Create a property called `marks`. Allow marks to be changed using a setter.
class Student:
    def __init__(self, marks):
        self._marks = marks
    @property
    def marks(self):
        return self._marks
    @marks.setter
    def marks(self, marks):
        self._marks = marks
student = Student(80)
print(student.marks)
student.marks = 90
print(student.marks)

### Q27. Create a Student class with `_percentage`. Use a setter to allow values only from 0 to 100.
class Student:
    def __init__(self, percentage):
        self._percentage = percentage
    @property
    def percentage(self):
        return self._percentage
    @percentage.setter
    def percentage(self, percentage):
        if 0 <= percentage <= 100:
            self._percentage = percentage
        else:
            print("Percentage must be between 0 and 100")
student = Student(80)
print(student.percentage)
student.percentage = 95
print(student.percentage)