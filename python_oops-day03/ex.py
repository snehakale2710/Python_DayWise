# Q1. Create a BankAccount class with a private __balance variable.
# Add methods to deposit, withdraw, and display the balance.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")
    def display_balance(self):
        print("Balance:", self.__balance)
account = BankAccount(5000)
account.deposit(1000)
account.withdraw(2000)
account.display_balance()

# Q2. Create a Student class with private __name and __marks variables.
# Use getter and setter methods to read and update them.
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks
    def get_name(self):
        return self.__name
    def get_marks(self):
        return self.__marks
    def set_name(self, name):
        self.__name = name
    def set_marks(self, marks):
        self.__marks = marks
student = Student("Sneha", 80)
print("Name:", student.get_name())
print("Marks:", student.get_marks())
student.set_marks(90)
print("Updated Marks:", student.get_marks())

# Q3. Create an Employee class with private __salary.
# Allow salary changes only through a setter that rejects negative values.
class Employee:
    def __init__(self, salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative")
employee = Employee(30000)
print("Salary:", employee.get_salary())
employee.set_salary(35000)
print("Updated Salary:", employee.get_salary())

# Q4. Create a Person class with private __age.
# Create methods to set age and check whether the person is eligible to vote.
class Person:
    def __init__(self, age):
        self.__age = age
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Invalid age")
    def check_vote(self):
        if self.__age >= 18:
            print("Eligible to vote")
        else:
            print("Not eligible to vote")
person = Person(20)
person.check_vote()
person.set_age(16)
person.check_vote()

# Q5. Create a Product class with private __price.
# Prevent the price from being set to zero or a negative number.
class Product:
    def __init__(self, price):
        self.__price = 0
        self.set_price(price)
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be greater than zero")
    def get_price(self):
        return self.__price

product = Product(500)
print("Price:", product.get_price())
product.set_price(800)
print("Updated Price:", product.get_price())

# Q6. Create a Mobile class with private __brand, __model, and __price.
# Add methods to set and display all details.
class Mobile:
    def __init__(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price
    def set_details(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price
    def display_details(self):
        print("Brand:", self.__brand)
        print("Model:", self.__model)
        print("Price:", self.__price)
mobile = Mobile("Samsung", "S24", 70000)
mobile.display_details()
mobile.set_details("OnePlus", "Nord", 25000)
mobile.display_details()

# Q7. Create a Car class with a private __speed.
# Provide accelerate() and brake() methods and prevent speed from becoming negative.
class Car:
    def __init__(self, speed):
        self.__speed = speed
    def accelerate(self, value):
        self.__speed += value
    def brake(self, value):
        self.__speed -= value
        if self.__speed < 0:
            self.__speed = 0
    def display_speed(self):
        print("Speed:", self.__speed)
car = Car(50)
car.accelerate(20)
car.display_speed()
car.brake(30)
car.display_speed()
car.brake(100)
car.display_speed()

# Q8. Create a Rectangle class with private __length and __width.
# Use methods to calculate area and perimeter.
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    def area(self):
        return self.__length * self.__width
    def perimeter(self):
        return 2 * (self.__length + self.__width)
rectangle = Rectangle(10, 5)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())

# Q9. Create a Circle class with private __radius.
# Use a setter to reject a radius less than or equal to zero.
class Circle:
    def __init__(self, radius):
        self.__radius = 0
        self.set_radius(radius)
    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Radius must be greater than zero")
    def area(self):
        return 3.14 * self.__radius * self.__radius
circle = Circle(5)
print("Area:", circle.area())
circle.set_radius(-2)

# Q10. Create an Account class with private __account_number and __balance.
# Display account information through a public method.
class Account:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    def display_account(self):
        print("Account Number:", self.__account_number)
        print("Balance:", self.__balance)
account = Account("1234567890", 25000)
account.display_account()

# Q11. Create a LibraryBook class with private __title and __issued.
# Add methods issue_book(), return_book(), and display_status().
class LibraryBook:
    def __init__(self, title):
        self.__title = title
        self.__issued = False
    def issue_book(self):
        if self.__issued == False:
            self.__issued = True
            print("Book issued")
        else:
            print("Book is already issued")
    def return_book(self):
        self.__issued = False
        print("Book returned")
    def display_status(self):
        print("Book:", self.__title)
        if self.__issued:
            print("Status: Issued")
        else:
            print("Status: Available")
book = LibraryBook("Python Programming")
book.display_status()
book.issue_book()
book.display_status()
book.return_book()
book.display_status()

# Q12. Create a StudentResult class with private marks for three subjects.
# Add methods to calculate total, percentage, and grade.
class StudentResult:
    def __init__(self, marks1, marks2, marks3):
        self.__marks1 = marks1
        self.__marks2 = marks2
        self.__marks3 = marks3
    def total(self):
        return self.__marks1 + self.__marks2 + self.__marks3
    def percentage(self):
        return self.total() / 3
    def grade(self):
        percentage = self.percentage()
        if percentage >= 75:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        else:
            return "D"
result = StudentResult(80, 75, 90)
print("Total:", result.total())
print("Percentage:", result.percentage())
print("Grade:", result.grade())

# Q13. Create a Login class with private __username and __password.
# Add a method to validate login credentials.
class Login:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    def validate_login(self, username, password):
        if username == self.__username and password == self.__password:
            print("Login successful")
        else:
            print("Invalid username or password")
login = Login("admin", "1234")
login.validate_login("admin", "1234")

# Q14. Create a User class with private __email and __password.
# Provide methods to change the password only after checking the old password.
class User:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password
    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password changed successfully")
        else:
            print("Old password is incorrect")
user = User("sneha@gmail.com", "1234")
user.change_password("1234", "5678")

# Q15. Create a Temperature class with private __celsius.
# Add methods to convert Celsius to Fahrenheit and Kelvin.
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    def to_fahrenheit(self):
        return (self.__celsius * 9 / 5) + 32
    def to_kelvin(self):
        return self.__celsius + 273.15
temperature = Temperature(25)
print("Fahrenheit:", temperature.to_fahrenheit())
print("Kelvin:", temperature.to_kelvin())

# Q16. Create a BankCustomer class with private __name and __pin.
# Add a method to verify the PIN without exposing it directly.
class BankCustomer:
    def __init__(self, name, pin):
        self.__name = name
        self.__pin = pin
    def verify_pin(self, pin):
        if pin == self.__pin:
            print("PIN is correct")
        else:
            print("Wrong PIN")
customer = BankCustomer("Sneha", 1234)
customer.verify_pin(1234)

# Q17. Create an ATM class with private __balance and __pin.
# Implement deposit, withdraw, and balance inquiry using public methods.
class ATM:
    def __init__(self, balance, pin):
        self.__balance = balance
        self.__pin = pin
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited")
    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                print("Amount withdrawn")
            else:
                print("Insufficient balance")
        else:
            print("Wrong PIN")
    def balance_inquiry(self, pin):
        if pin == self.__pin:
            print("Balance:", self.__balance)
        else:
            print("Wrong PIN")
atm = ATM(10000, 1234)
atm.deposit(2000)
atm.withdraw(3000, 1234)
atm.balance_inquiry(1234)

# Q18. Create an Employee class with private __name, __department, and __salary.
# Add a method to calculate annual salary.
class EmployeeDetails:
    def __init__(self, name, department, salary):
        self.__name = name
        self.__department = department
        self.__salary = salary
    def annual_salary(self):
        return self.__salary * 12
    def display(self):
        print("Name:", self.__name)
        print("Department:", self.__department)
        print("Salary:", self.__salary)
employee_details = EmployeeDetails("Rahul", "IT", 30000)
employee_details.display()
print("Annual Salary:", employee_details.annual_salary())

# Q19. Create a HospitalPatient class with private __name, __age, and __bill.
# Add methods to add charges and display the bill.
class HospitalPatient:
    def __init__(self, name, age, bill):
        self.__name = name
        self.__age = age
        self.__bill = bill
    def add_charges(self, amount):
        if amount > 0:
            self.__bill += amount
    def display_bill(self):
        print("Patient Name:", self.__name)
        print("Age:", self.__age)
        print("Bill:", self.__bill)
patient = HospitalPatient("Amit", 25, 5000)
patient.add_charges(2000)
patient.display_bill()

# Q20. Create a ShoppingCart class with private __items and __total.
# Add methods to add products, remove products, and calculate the total.
class ShoppingCart:
    def __init__(self):
        self.__items = []
        self.__total = 0
    def add_product(self, name, price):
        self.__items.append(name)
        self.__total += price
    def remove_product(self, name, price):
        if name in self.__items:
            self.__items.remove(name)
            self.__total -= price
    def calculate_total(self):
        return self.__total
    def display_items(self):
        print("Items:", self.__items)
        print("Total:", self.__total)
cart = ShoppingCart()
cart.add_product("Shirt", 1000)
cart.add_product("Shoes", 2000)
cart.display_items()
cart.remove_product("Shirt", 1000)
cart.display_items()

# Q21. Create a Course class with private __course_name and __fees.
# Add validation so fees cannot be negative.
class Course:
    def __init__(self, course_name, fees):
        self.__course_name = course_name
        self.__fees = 0
        self.set_fees(fees)
    def set_fees(self, fees):
        if fees >= 0:
            self.__fees = fees
        else:
            print("Fees cannot be negative")
    def display(self):
        print("Course:", self.__course_name)
        print("Fees:", self.__fees)
course = Course("Python", 5000)
course.display()
course.set_fees(-1000)

# Q22. Create a Vehicle class with private __fuel.
# Add methods refuel(), drive(), and show_fuel().
# Prevent driving when fuel is insufficient.
class Vehicle:
    def __init__(self, fuel):
        self.__fuel = fuel
    def refuel(self, amount):
        if amount > 0:
            self.__fuel += amount
    def drive(self, fuel_required):
        if fuel_required <= self.__fuel:
            self.__fuel -= fuel_required
            print("Vehicle driven")
        else:
            print("Insufficient fuel")
    def show_fuel(self):
        print("Fuel:", self.__fuel)
vehicle = Vehicle(20)
vehicle.show_fuel()
vehicle.drive(5)
vehicle.show_fuel()
vehicle.refuel(10)
vehicle.show_fuel()

# Q23. Create a Wallet class with private __money.
# Add add_money() and spend_money() methods with validation.
class Wallet:
    def __init__(self, money):
        self.__money = money
    def add_money(self, amount):
        if amount > 0:
            self.__money += amount
    def spend_money(self, amount):
        if amount > 0 and amount <= self.__money:
            self.__money -= amount
        else:
            print("Invalid amount")
    def display(self):
        print("Money:", self.__money)
wallet = Wallet(1000)
wallet.add_money(500)
wallet.spend_money(200)
wallet.display()

# Q24. Create a Salary class with private __basic_salary.
# Add methods to calculate HRA, DA, and gross salary.
class Salary:
    def __init__(self, basic_salary):
        self.__basic_salary = basic_salary
    def calculate_hra(self):
        return self.__basic_salary * 0.20
    def calculate_da(self):
        return self.__basic_salary * 0.10
    def gross_salary(self):
        return self.__basic_salary + self.calculate_hra() + self.calculate_da()
salary = Salary(30000)
print("HRA:", salary.calculate_hra())
print("DA:", salary.calculate_da())
print("Gross Salary:", salary.gross_salary())

# Q25. Create a Result class with private __marks.
# Update marks only when the value is between 0 and 100.
class Result:
    def __init__(self, marks):
        self.__marks = 0
        self.update_marks(marks)
    def update_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be between 0 and 100")
    def display(self):
        print("Marks:", self.__marks)
result = Result(80)
result.display()
result.update_marks(95)
result.display()
result.update_marks(120)

# Q26. Create a DoorLock class with private __password.
# Add methods lock(), unlock(), and change_password().
class DoorLock:
    def __init__(self, password):
        self.__password = password
        self.__locked = True
    def lock(self):
        self.__locked = True
        print("Door locked")
    def unlock(self, password):
        if password == self.__password:
            self.__locked = False
            print("Door unlocked")
        else:
            print("Wrong password")
    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password changed")
        else:
            print("Wrong old password")
door = DoorLock("1234")
door.unlock("1234")
door.change_password("1234", "5678")
door.lock()

# Q27. Create a Contact class with private __phone_number.
# Validate that the phone number contains exactly 10 digits before storing it.
class Contact:
    def __init__(self, phone_number):
        self.__phone_number = ""
        self.set_phone_number(phone_number)
    def set_phone_number(self, phone_number):
        phone_number = str(phone_number)
        if phone_number.isdigit() and len(phone_number) == 10:
            self.__phone_number = phone_number
        else:
            print("Invalid phone number")
    def display(self):
        print("Phone Number:", self.__phone_number)
contact = Contact("9876543210")
contact.display()

# Q28. Create a Movie class with private __rating.
# Allow ratings only from 1 to 5.
class Movie:
    def __init__(self, rating):
        self.__rating = 0
        self.set_rating(rating)
    def set_rating(self, rating):
        if 1 <= rating <= 5:
            self.__rating = rating
        else:
            print("Rating must be between 1 and 5")
    def display_rating(self):
        print("Rating:", self.__rating)
movie = Movie(4)
movie.display_rating()
movie.set_rating(6)

# Q29. Create a Bank class with private __interest_rate.
# Add a method to calculate simple interest for a given principal and time.
class Bank:
    def __init__(self, interest_rate):
        self.__interest_rate = interest_rate
    def simple_interest(self, principal, time):
        return principal * self.__interest_rate * time / 100
bank = Bank(5)
print("Simple Interest:", bank.simple_interest(10000, 2))

# Q30. Create an Inventory class with private __quantity.
# Add stock and sell methods, preventing quantity from becoming negative.
class Inventory:
    def __init__(self, quantity):
        self.__quantity = quantity
    def add_stock(self, quantity):
        if quantity > 0:
            self.__quantity += quantity
    def sell(self, quantity):
        if quantity <= self.__quantity:
            self.__quantity -= quantity
        else:
            print("Insufficient stock")
    def display(self):
        print("Quantity:", self.__quantity)
inventory = Inventory(50)
inventory.add_stock(20)
inventory.sell(10)
inventory.display()

# Q31. Create a School class with private __school_name and __students.
# Add methods to add students and display the student count.
class School:
    def __init__(self, school_name):
        self.__school_name = school_name
        self.__students = []
    def add_student(self, name):
        self.__students.append(name)
    def display_count(self):
        print("School:", self.__school_name)
        print("Student Count:", len(self.__students))
school = School("ABC School")
school.add_student("Amit")
school.add_student("Sneha")
school.add_student("Rahul")
school.display_count()

# Q32. Create a Flight class with private __available_seats.
# Add booking and cancellation methods with proper validation.
class Flight:
    def __init__(self, seats):
        self.__available_seats = seats
    def book_seat(self):
        if self.__available_seats > 0:
            self.__available_seats -= 1
            print("Seat booked")
        else:
            print("No seats available")
    def cancel_seat(self):
        self.__available_seats += 1
        print("Booking cancelled")
    def display_seats(self):
        print("Available Seats:", self.__available_seats)
flight = Flight(100)
flight.book_seat()
flight.display_seats()
flight.cancel_seat()
flight.display_seats()

# Q33. Create a BusTicket class with private __passenger_name and __fare.
# Add methods to apply a discount and display the final fare.
class BusTicket:
    def __init__(self, passenger_name, fare):
        self.__passenger_name = passenger_name
        self.__fare = fare
    def apply_discount(self, discount):
        if 0 <= discount <= 100:
            self.__fare -= self.__fare * discount / 100
        else:
            print("Invalid discount")
    def display(self):
        print("Passenger:", self.__passenger_name)
        print("Final Fare:", self.__fare)
ticket = BusTicket("Sneha", 500)
ticket.apply_discount(10)
ticket.display()

# Q34. Create a RestaurantBill class with private __amount.
# Add methods to add item prices, apply GST, and display the final bill.
class RestaurantBill:
    def __init__(self):
        self.__amount = 0
    def add_item(self, price):
        if price > 0:
            self.__amount += price
    def apply_gst(self):
        self.__amount += self.__amount * 0.05
    def display_bill(self):
        print("Final Bill:", self.__amount)
restaurant_bill = RestaurantBill()
restaurant_bill.add_item(500)
restaurant_bill.add_item(200)
restaurant_bill.apply_gst()
restaurant_bill.display_bill()

# Q35. Create an ElectricityBill class with private __units.
# Calculate the bill using different rates for different unit ranges.
class ElectricityBill:
    def __init__(self, units):
        self.__units = units
    def calculate_bill(self):
        if self.__units <= 100:
            bill = self.__units * 5
        elif self.__units <= 200:
            bill = (100 * 5) + ((self.__units - 100) * 7)
        else:
            bill = (100 * 5) + (100 * 7) + ((self.__units - 200) * 10)
        return bill
electricity = ElectricityBill(250)
print("Electricity Bill:", electricity.calculate_bill())

# Q36. Create a CreditCard class with private __limit and __used_amount.
# Prevent purchases that exceed the available limit.
class CreditCard:
    def __init__(self, limit):
        self.__limit = limit
        self.__used_amount = 0
    def purchase(self, amount):
        available = self.__limit - self.__used_amount
        if amount <= available:
            self.__used_amount += amount
            print("Purchase successful")
        else:
            print("Purchase exceeds available limit")
    def display(self):
        print("Credit Limit:", self.__limit)
        print("Used Amount:", self.__used_amount)
        print("Available Limit:", self.__limit - self.__used_amount)
credit_card = CreditCard(50000)
credit_card.purchase(10000)
credit_card.display()

# Q37. Create a CourseRegistration class with private __student_name and __course.
# Add methods to register and display registration details.
class CourseRegistration:
    def __init__(self, student_name, course):
        self.__student_name = student_name
        self.__course = course
        self.__registered = False
    def register(self):
        self.__registered = True
        print("Registration successful")
    def display(self):
        print("Student Name:", self.__student_name)
        print("Course:", self.__course)
        if self.__registered:
            print("Status: Registered")
        else:
            print("Status: Not Registered")
registration = CourseRegistration("Sneha", "MCA")
registration.register()
registration.display()

# Q38. Create a FreelanceProject class with private __client_name and __payment.
# Add a method to calculate payment after tax deduction.
class FreelanceProject:
    def __init__(self, client_name, payment):
        self.__client_name = client_name
        self.__payment = payment
    def payment_after_tax(self):
        tax = self.__payment * 0.10
        return self.__payment - tax
    def display(self):
        print("Client:", self.__client_name)
        print("Payment:", self.__payment)
project = FreelanceProject("ABC Company", 50000)
project.display()
print("Payment After Tax:", project.payment_after_tax())

# Q39. Create a SalaryAccount class with private __balance.
# Add methods for credit, debit, and monthly interest calculation.
class SalaryAccount:
    def __init__(self, balance):
        self.__balance = balance
    def credit(self, amount):
        if amount > 0:
            self.__balance += amount
    def debit(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid debit")
    def monthly_interest(self):
        return self.__balance * 0.01
    def display_balance(self):
        print("Balance:", self.__balance)
salary_account = SalaryAccount(30000)
salary_account.credit(5000)
salary_account.debit(2000)
salary_account.display_balance()
print("Monthly Interest:", salary_account.monthly_interest())

# Q40. Create a SecureFile class with private __filename and __password.
# Add a method to open the file only after password verification.
class SecureFile:
    def __init__(self, filename, password):
        self.__filename = filename
        self.__password = password
    def open_file(self, password):
        if password == self.__password:
            print("File opened:", self.__filename)
        else:
            print("Wrong password")
secure_file = SecureFile("data.txt", "1234")
secure_file.open_file("1234")