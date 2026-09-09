# ============================================================
# CLASS, OBJECT & INSTANCE VARIABLES
# ============================================================

# 1. Create a Student class with instance variables name, age, and marks. Create one object and display all details.
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

student = Student("Sneha", 21, 85)
print(student.name, student.age, student.marks)


# 2. Create an Employee class with name, salary, and department. Display employee details.
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

employee = Employee("Rahul", 30000, "IT")
print(employee.name, employee.salary, employee.department)


# 3. Create a Car class with brand, model, and price. Create two objects and display their details.
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

car1 = Car("Toyota", "Fortuner", 4000000)
car2 = Car("Honda", "City", 1500000)

print(car1.brand, car1.model, car1.price)
print(car2.brand, car2.model, car2.price)


# 4. Create a Book class with title, author, and price. Create an object and display the information.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

book = Book("Wings of Fire", "A. P. J. Abdul Kalam", 350)
print(book.title, book.author, book.price)


# 5. Create a Mobile class with brand, model, and price. Display mobile details.
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

mobile = Mobile("Samsung", "Galaxy A12", 15000)
print(mobile.brand, mobile.model, mobile.price)


# 6. Create a Product class with product_name, price, and quantity. Display all values.
class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

product = Product("Laptop", 50000, 2)
print(product.product_name, product.price, product.quantity)


# 7. Create a Person class with name, age, and city. Create three objects and display their information.
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person1 = Person("Amit", 22, "Pune")
person2 = Person("Neha", 23, "Mumbai")
person3 = Person("Riya", 21, "Nashik")

print(person1.name, person1.age, person1.city)
print(person2.name, person2.age, person2.city)
print(person3.name, person3.age, person3.city)


# 8. Create a Laptop class with brand, ram, storage, and price. Display laptop details.
class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

laptop = Laptop("Lenovo", "16GB", "512GB", 60000)
print(laptop.brand, laptop.ram, laptop.storage, laptop.price)


# 9. Create a Movie class with name, actor, actress, and rating. Display movie information.
class Movie:
    def __init__(self, name, actor, actress, rating):
        self.name = name
        self.actor = actor
        self.actress = actress
        self.rating = rating

movie = Movie("Dangal", "Aamir Khan", "Fatima Sana Shaikh", 8.3)
print(movie.name, movie.actor, movie.actress, movie.rating)


# 10. Create a BankAccount class with account_holder, account_number, and balance. Display account details.
class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

account = BankAccount("Sneha", "1234567890", 25000)
print(account.account_holder, account.account_number, account.balance)


# 11. Create a Teacher class with name, subject, and salary. Create two objects.
class Teacher:
    def __init__(self, name, subject, salary):
        self.name = name
        self.subject = subject
        self.salary = salary

teacher1 = Teacher("Anita", "Python", 40000)
teacher2 = Teacher("Raj", "Maths", 45000)

print(teacher1.name, teacher1.subject, teacher1.salary)
print(teacher2.name, teacher2.subject, teacher2.salary)


# 12. Create a CollegeStudent class with name, roll_no, course, and year.
class CollegeStudent:
    def __init__(self, name, roll_no, course, year):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.year = year

college_student = CollegeStudent("Sneha", 101, "MCA", 1)
print(college_student.name, college_student.roll_no, college_student.course, college_student.year)


# 13. Create a HospitalPatient class with name, age, disease, and room_no.
class HospitalPatient:
    def __init__(self, name, age, disease, room_no):
        self.name = name
        self.age = age
        self.disease = disease
        self.room_no = room_no

patient = HospitalPatient("Rahul", 35, "Fever", 205)
print(patient.name, patient.age, patient.disease, patient.room_no)


# 14. Create a Laptop class and create five different laptop objects with different values.
class LaptopFive:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

laptop1 = LaptopFive("Dell", "8GB", "512GB", 45000)
laptop2 = LaptopFive("HP", "16GB", "512GB", 55000)
laptop3 = LaptopFive("Lenovo", "16GB", "1TB", 65000)
laptop4 = LaptopFive("Asus", "8GB", "512GB", 50000)
laptop5 = LaptopFive("Acer", "16GB", "1TB", 70000)

print(laptop1.brand, laptop1.ram, laptop1.storage, laptop1.price)
print(laptop2.brand, laptop2.ram, laptop2.storage, laptop2.price)
print(laptop3.brand, laptop3.ram, laptop3.storage, laptop3.price)
print(laptop4.brand, laptop4.ram, laptop4.storage, laptop4.price)
print(laptop5.brand, laptop5.ram, laptop5.storage, laptop5.price)


# 15. Create a Bike class with brand, model, color, and price.
class Bike:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

bike = Bike("Royal Enfield", "Classic 350", "Black", 200000)
print(bike.brand, bike.model, bike.color, bike.price)


# 16. Create a Company class with company_name, location, and employees.
class Company:
    def __init__(self, company_name, location, employees):
        self.company_name = company_name
        self.location = location
        self.employees = employees

company = Company("Infosys", "Pune", 5000)
print(company.company_name, company.location, company.employees)


# 17. Create a Course class with course_name, duration, and fees.
class Course:
    def __init__(self, course_name, duration, fees):
        self.course_name = course_name
        self.duration = duration
        self.fees = fees

course = Course("Python", "6 Months", 30000)
print(course.course_name, course.duration, course.fees)


# 18. Create a Restaurant class with name, location, and rating.
class Restaurant:
    def __init__(self, name, location, rating):
        self.name = name
        self.location = location
        self.rating = rating

restaurant = Restaurant("Food Palace", "Pune", 4.5)
print(restaurant.name, restaurant.location, restaurant.rating)


# 19. Create a Flight class with flight_no, source, destination, and price.
class Flight:
    def __init__(self, flight_no, source, destination, price):
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.price = price

flight = Flight("AI101", "Pune", "Delhi", 5500)
print(flight.flight_no, flight.source, flight.destination, flight.price)


# 20. Create a Hotel class with name, location, room_type, and price.
class Hotel:
    def __init__(self, name, location, room_type, price):
        self.name = name
        self.location = location
        self.room_type = room_type
        self.price = price

hotel = Hotel("Grand Hotel", "Pune", "Deluxe", 4000)
print(hotel.name, hotel.location, hotel.room_type, hotel.price)


# ============================================================
# INSTANCE METHODS
# ============================================================

# 21. Create a Student class with a display() method to display student details.
class StudentMethod:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(self.name, self.age, self.marks)

student_method = StudentMethod("Sneha", 21, 85)
student_method.display()


# 22. Create an Employee class with a display_salary() method.
class EmployeeMethod:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print("Salary:", self.salary)

employee_method = EmployeeMethod("Rahul", 35000)
employee_method.display_salary()


# 23. Create a Car class with a start() method that prints "Car Started".
class CarMethod:
    def start(self):
        print("Car Started")

car_method = CarMethod()
car_method.start()


# 24. Create a Mobile class with a call() method that prints a calling message.
class MobileMethod:
    def __init__(self, name):
        self.name = name

    def call(self):
        print("Calling from", self.name)

mobile_method = MobileMethod("Samsung")
mobile_method.call()


# 25. Create a Person class with a greet() method.
class PersonMethod:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

person_method = PersonMethod("Sneha")
person_method.greet()


# 26. Create a BankAccount class with a display_balance() method.
class BankAccountMethod:
    def __init__(self, balance):
        self.balance = balance

    def display_balance(self):
        print("Balance:", self.balance)

account_method = BankAccountMethod(25000)
account_method.display_balance()


# 27. Create a Book class with a display_book() method.
class BookMethod:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book(self):
        print("Title:", self.title)
        print("Author:", self.author)

book_method = BookMethod("Wings of Fire", "A. P. J. Abdul Kalam")
book_method.display_book()


# 28. Create a Product class with a display_product() method.
class ProductMethod:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print("Product:", self.product_name)
        print("Price:", self.price)

product_method = ProductMethod("Laptop", 50000)
product_method.display_product()


# ============================================================
# self KEYWORD PRACTICE
# ============================================================

# 29. Create a Student class and use self.name and self.marks to display student details.
class StudentSelf:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)

student_self = StudentSelf("Sneha", 90)
student_self.display()


# 30. Create an Employee class and use self to access employee salary.
class EmployeeSelf:
    def __init__(self, salary):
        self.salary = salary

    def display_salary(self):
        print("Salary:", self.salary)

employee_self = EmployeeSelf(40000)
employee_self.display_salary()


# 31. Create a Car class and use self.brand and self.model inside a method.
class CarSelf:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(self.brand, self.model)

car_self = CarSelf("Toyota", "Fortuner")
car_self.display()


# 32. Create a Product class and use self.price inside a method to calculate total price.
class ProductSelf:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        print("Total Price:", self.price * self.quantity)

product_self = ProductSelf(500, 3)
product_self.calculate_total()


# 33. Create a Student class with a method that prints "Hello" followed by the student's name using self.
class StudentHello:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello", self.name)

student_hello = StudentHello("Sneha")
student_hello.hello()


# 34. Create a BankAccount class and use self.balance to display the current balance.
class BankAccountSelf:
    def __init__(self, balance):
        self.balance = balance

    def display(self):
        print("Current Balance:", self.balance)

account_self = BankAccountSelf(30000)
account_self.display()


# 35. Create a Book class and use self.title and self.author in a method.
class BookSelf:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(self.title, self.author)

book_self = BookSelf("Harry Potter", "J. K. Rowling")
book_self.display()


# 36. Create a Mobile class and use self.price to display mobile price.
class MobileSelf:
    def __init__(self, price):
        self.price = price

    def display_price(self):
        print("Mobile Price:", self.price)

mobile_self = MobileSelf(20000)
mobile_self.display_price()


# ============================================================
# MULTIPLE METHODS IN ONE CLASS
# ============================================================

# 37. Create a Calculator class containing add(), subtract(), multiply(), and divide() methods.
class Calculator:
    def add(self, a, b):
        print("Addition:", a + b)

    def subtract(self, a, b):
        print("Subtraction:", a - b)

    def multiply(self, a, b):
        print("Multiplication:", a * b)

    def divide(self, a, b):
        print("Division:", a / b)

calculator = Calculator()
calculator.add(10, 5)
calculator.subtract(10, 5)
calculator.multiply(10, 5)
calculator.divide(10, 5)


# 38. Create a Student class containing display(), calculate_total(), and calculate_percentage() methods.
class StudentMultiple:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def display(self):
        print("Name:", self.name)

    def calculate_total(self):
        return self.marks1 + self.marks2 + self.marks3

    def calculate_percentage(self):
        return self.calculate_total() / 3

student_multiple = StudentMultiple("Sneha", 85, 90, 95)
student_multiple.display()
print("Total:", student_multiple.calculate_total())
print("Percentage:", student_multiple.calculate_percentage())


# 39. Create an Employee class containing display(), calculate_annual_salary(), and calculate_bonus() methods.
class EmployeeMultiple:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Monthly Salary:", self.salary)

    def calculate_annual_salary(self):
        return self.salary * 12

    def calculate_bonus(self):
        return self.salary * 0.10

employee_multiple = EmployeeMultiple("Rahul", 40000)
employee_multiple.display()
print("Annual Salary:", employee_multiple.calculate_annual_salary())
print("Bonus:", employee_multiple.calculate_bonus())


# 40. Create a BankAccount class containing deposit(), withdraw(), and display_balance() methods.
class BankAccountMultiple:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print("Balance:", self.balance)

bank_multiple = BankAccountMultiple(10000)
bank_multiple.deposit(5000)
bank_multiple.withdraw(2000)
bank_multiple.display_balance()


# 41. Create a Rectangle class containing area(), perimeter(), and display() methods.
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def display(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())

rectangle = Rectangle(10, 5)
rectangle.display()


# 42. Create a Circle class containing area(), circumference(), and display() methods.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius

    def display(self):
        print("Radius:", self.radius)
        print("Area:", self.area())
        print("Circumference:", self.circumference())

circle = Circle(7)
circle.display()


# 43. Create a Product class containing display(), calculate_total(), and apply_discount() methods.
class ProductMultiple:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def display(self):
        print("Product:", self.product_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount(self, discount):
        total = self.calculate_total()
        return total - (total * discount / 100)

product_multiple = ProductMultiple("Laptop", 50000, 2)
product_multiple.display()
print("Total:", product_multiple.calculate_total())
print("After Discount:", product_multiple.apply_discount(10))