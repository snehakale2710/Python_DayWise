# Q1. Create a Student class and create one object. Display the student's name, age, and course.

class Student:
    name = "Sneha"
    age = 21
    course = "MCA"

student1 = Student()

print("Name:", student1.name)
print("Age:", student1.age)
print("Course:", student1.course)


# Q2. Create an Employee class with a display() method. Display employee name, salary, and department.

class Employee:
    name = "Rahul"
    salary = 30000
    department = "IT"

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)

employee1 = Employee()
employee1.display()


# Q3. Create a Car class with two methods: start() and stop(). Call both methods using an object.

class Car:
    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

car1 = Car()
car1.start()
car1.stop()


# Q4. Create a Mobile class with methods call() and message(). Call both methods using an object.

class Mobile:
    def call(self):
        print("Calling...")

    def message(self):
        print("Sending Message...")

mobile1 = Mobile()
mobile1.call()
mobile1.message()


# Q5. Create a Book class with a display() method. Display book title, author, and price.

class Book:
    title = "Python Programming"
    author = "John Smith"
    price = 500

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

book1 = Book()
book1.display()


# Q6. Create a BankAccount class with methods deposit() and withdraw(). Display suitable messages when each method is called.

class BankAccount:
    def deposit(self):
        print("Amount Deposited Successfully")

    def withdraw(self):
        print("Amount Withdrawn Successfully")

account1 = BankAccount()
account1.deposit()
account1.withdraw()


# Q7. Create a Calculator class with methods add(), subtract(), multiply(), and divide().

class Calculator:
    def add(self, a, b):
        print("Addition:", a + b)

    def subtract(self, a, b):
        print("Subtraction:", a - b)

    def multiply(self, a, b):
        print("Multiplication:", a * b)

    def divide(self, a, b):
        print("Division:", a / b)

calculator1 = Calculator()
calculator1.add(10, 5)
calculator1.subtract(10, 5)
calculator1.multiply(10, 5)
calculator1.divide(10, 5)


# Q8. Create a College class with a method college_details(). Display college name, city, and course.

class College:
    def college_details(self):
        print("College Name: Greenfingers College")
        print("City: Akluj")
        print("Course: MCA")

college1 = College()
college1.college_details()


# Q9. Create a Product class with a display() method. Display product name, price, and quantity.

class Product:
    name = "Laptop"
    price = 50000
    quantity = 2

    def display(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

product1 = Product()
product1.display()


# Q10. Create a Customer class with methods show_customer(), place_order(), and cancel_order().

class Customer:
    def show_customer(self):
        print("Customer Details")

    def place_order(self):
        print("Order Placed Successfully")

    def cancel_order(self):
        print("Order Cancelled Successfully")

customer1 = Customer()
customer1.show_customer()
customer1.place_order()
customer1.cancel_order()


# Q11. Create a Laptop class with methods power_on() and power_off().

class Laptop:
    def power_on(self):
        print("Laptop is ON")

    def power_off(self):
        print("Laptop is OFF")

laptop1 = Laptop()
laptop1.power_on()
laptop1.power_off()


# Q12. Create a Teacher class with a method display_details(). Display teacher name, subject, and experience.

class Teacher:
    def display_details(self):
        print("Teacher Name: Priya")
        print("Subject: Python")
        print("Experience: 5 Years")

teacher1 = Teacher()
teacher1.display_details()


# Q13. Create a Company class with a method company_details(). Display company name, location, and employees.

class Company:
    def company_details(self):
        print("Company Name: Intellisys")
        print("Location: Pune")
        print("Employees: 50")

company1 = Company()
company1.company_details()


# Q14. Create a Movie class with a method display(). Display movie name, actor, actress, and rating.

class Movie:
    def display(self):
        print("Movie Name: Jawan")
        print("Actor: Shah Rukh Khan")
        print("Actress: Nayanthara")
        print("Rating: 8/10")

movie1 = Movie()
movie1.display()