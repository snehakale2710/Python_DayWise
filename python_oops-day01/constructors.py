# Q15. Create a Student class using a constructor that accepts name, age, and course. Display all details.

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

student1 = Student("Sneha", 21, "MCA")
student1.display()


# Q16. Create an Employee class using a constructor that accepts employee name, salary, and department.

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)

employee1 = Employee("Rahul", 30000, "IT")
employee1.display()


# Q17. Create a Car class using a constructor that accepts company, model, and price.

class Car:
    def __init__(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display(self):
        print("Company:", self.company)
        print("Model:", self.model)
        print("Price:", self.price)

car1 = Car("Toyota", "Fortuner", 3500000)
car1.display()


# Q18. Create a Mobile class using a constructor that accepts brand, model, and price.

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

mobile1 = Mobile("Samsung", "Galaxy A12", 15000)
mobile1.display()


# Q19. Create a Book class using a constructor that accepts title, author, and price.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

book1 = Book("Python Programming", "John Smith", 500)
book1.display()


# Q20. Create a Product class using a constructor that accepts product name, price, and quantity. Calculate the total price.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        total = self.price * self.quantity
        print("Product Name:", self.name)
        print("Total Price:", total)

product1 = Product("Laptop", 50000, 2)
product1.total_price()


# Q21. Create a BankAccount class using a constructor that accepts account holder name and balance. Create methods for deposit, withdrawal, and balance display.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)

account1 = BankAccount("Sneha", 10000)
account1.deposit(5000)
account1.withdraw(2000)
account1.display_balance()


# Q22. Create a Rectangle class using a constructor that accepts length and width. Calculate area and perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)

    def perimeter(self):
        print("Perimeter:", 2 * (self.length + self.width))

rectangle1 = Rectangle(10, 5)
rectangle1.area()
rectangle1.perimeter()


# Q23. Create a Circle class using a constructor that accepts radius. Calculate area and circumference.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area:", math.pi * self.radius * self.radius)

    def circumference(self):
        print("Circumference:", 2 * math.pi * self.radius)

circle1 = Circle(5)
circle1.area()
circle1.circumference()


# Q24. Create a Student class using a constructor that accepts name and three subject marks. Calculate total and percentage.

class StudentMarks:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def result(self):
        total = self.marks1 + self.marks2 + self.marks3
        percentage = total / 3

        print("Name:", self.name)
        print("Total:", total)
        print("Percentage:", percentage)

student2 = StudentMarks("Sneha", 80, 75, 90)
student2.result()


# Q25. Create an Employee class using a constructor that accepts name and monthly salary. Calculate annual salary.

class EmployeeSalary:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        annual = self.monthly_salary * 12

        print("Employee Name:", self.name)
        print("Annual Salary:", annual)

employee2 = EmployeeSalary("Rahul", 30000)
employee2.annual_salary()


# Q26. Create a ShoppingCart class using a constructor that accepts product name, price, and quantity. Calculate the total bill.

class ShoppingCart:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def total_bill(self):
        total = self.price * self.quantity

        print("Product Name:", self.product_name)
        print("Total Bill:", total)

cart1 = ShoppingCart("Shoes", 2000, 3)
cart1.total_bill()


# Q27. Create a Laptop class using a constructor that accepts brand, RAM, storage, and price. Display all details.

class LaptopDetails:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print("Price:", self.price)

laptop2 = LaptopDetails("Lenovo", "16GB", "512GB SSD", 60000)
laptop2.display()


# Q28. Create a Customer class using a constructor that accepts customer ID, name, mobile number, and city. Display customer details.

class CustomerDetails:
    def __init__(self, customer_id, name, mobile, city):
        self.customer_id = customer_id
        self.name = name
        self.mobile = mobile
        self.city = city

    def display(self):
        print("Customer ID:", self.customer_id)
        print("Name:", self.name)
        print("Mobile Number:", self.mobile)
        print("City:", self.city)

customer2 = CustomerDetails(101, "Sneha", "9876543210", "Pune")
customer2.display()


# Q29. Create a Salary class using a constructor that accepts employee name and basic salary. Calculate HRA, DA, and Gross Salary.

class Salary:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate(self):
        hra = self.basic_salary * 20 / 100
        da = self.basic_salary * 10 / 100
        gross_salary = self.basic_salary + hra + da

        print("Employee Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", hra)
        print("DA:", da)
        print("Gross Salary:", gross_salary)

salary1 = Salary("Sneha", 30000)
salary1.calculate()


# Q30. Create a Result class using a constructor that accepts student name and marks of five subjects. Calculate total, percentage, and pass/fail result.

class Result:
    def __init__(self, name, m1, m2, m3, m4, m5):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5

    def calculate(self):
        total = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        percentage = total / 5

        if percentage >= 40:
            result = "Pass"
        else:
            result = "Fail"

        print("Student Name:", self.name)
        print("Total:", total)
        print("Percentage:", percentage)
        print("Result:", result)

result1 = Result("Sneha", 80, 75, 85, 70, 90)
result1.calculate()


# Q31. Create a Product class using a constructor that accepts product name, price, and discount percentage. Calculate the final price after discount.

class ProductDiscount:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def final_price(self):
        discount_amount = self.price * self.discount / 100
        final_price = self.price - discount_amount

        print("Product Name:", self.name)
        print("Original Price:", self.price)
        print("Discount Amount:", discount_amount)
        print("Final Price:", final_price)

product2 = ProductDiscount("Shoes", 2000, 10)
product2.final_price()


# Q32. Create an ElectricityBill class using a constructor that accepts customer name and units consumed. Calculate the electricity bill based on units.

class ElectricityBill:
    def __init__(self, name, units):
        self.name = name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 5
        elif self.units <= 200:
            bill = (100 * 5) + ((self.units - 100) * 7)
        else:
            bill = (100 * 5) + (100 * 7) + ((self.units - 200) * 10)

        print("Customer Name:", self.name)
        print("Units Consumed:", self.units)
        print("Electricity Bill:", bill)

bill1 = ElectricityBill("Sneha", 250)
bill1.calculate_bill()


# Q33. Create a Travel class using a constructor that accepts passenger name, source, destination, and ticket price. Display the ticket details.

class Travel:
    def __init__(self, passenger, source, destination, ticket_price):
        self.passenger = passenger
        self.source = source
        self.destination = destination
        self.ticket_price = ticket_price

    def display(self):
        print("Passenger Name:", self.passenger)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print("Ticket Price:", self.ticket_price)

travel1 = Travel("Sneha", "Pune", "Mumbai", 500)
travel1.display()


# Q34. Create a BankAccount class and create 3 objects with different account holder names and balances. Display the details of all three accounts.

class BankAccountDetails:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)

account1 = BankAccountDetails("Sneha", 10000)
account2 = BankAccountDetails("Rahul", 15000)
account3 = BankAccountDetails("Priya", 20000)

account1.display()
account2.display()
account3.display()