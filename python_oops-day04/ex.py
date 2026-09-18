## Encapsulation
### Q1. Create a Student class with private marks. Create getter and setter methods for marks.
class Student:
    def __init__(self, marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    def set_marks(self, marks):
        self.__marks = marks
student = Student(85)
print(student.get_marks())
student.set_marks(90)
print(student.get_marks())

### Q2. Create a BankAccount class with private balance. Create deposit and withdrawal methods.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance
account = BankAccount(5000)
account.deposit(2000)
account.withdraw(1000)
print("Balance:", account.get_balance())

### Q3. Create an Employee class with private salary.
class Employee:
    def __init__(self, salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        self.__salary = salary
employee = Employee(30000)
print(employee.get_salary())
employee.set_salary(40000)
print(employee.get_salary())

# Inheritance
### Q4. Create Person → Student inheritance.
class Person:
    def show_person(self):
        print("I am a person")
class Student(Person):
    def show_student(self):
        print("I am a student")
student = Student()
student.show_person()
student.show_student()

### Q5. Create Vehicle → Car inheritance.
class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
car = Car()
car.start()
car.drive()

### Q6. Create Employee → Developer inheritance.
class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def code(self):
        print("Developer is coding")
developer = Developer()
developer.work()
developer.code()

### Q7. Create multilevel inheritance Animal → Dog → Puppy.
class Animal:
    def eat(self):
        print("Animal eats")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
class Puppy(Dog):
    def play(self):
        print("Puppy plays")
puppy = Puppy()
puppy.eat()
puppy.bark()
puppy.play()

### Q8. Create multiple inheritance using Father, Mother, and Child.
class Father:
    def father_property(self):
        print("Father's property")
class Mother:
    def mother_property(self):
        print("Mother's property")
class Child(Father, Mother):
    def child_property(self):
        print("Child's property")
child = Child()
child.father_property()
child.mother_property()
child.child_property()

# Polymorphism
### Q9. Create Dog, Cat, and Cow classes with sound().
class Dog:
    def sound(self):
        print("Dog says Woof")
class Cat:
    def sound(self):
        print("Cat says Meow")
class Cow:
    def sound(self):
        print("Cow says Moo")
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.sound()

### Q10. Create Shape, Circle, and Rectangle with area().
class Shape:
    def area(self):
        print("Shape area")
class Circle(Shape):
    def area(self):
        print("Circle area:", 3.14 * 5 * 5)
class Rectangle(Shape):
    def area(self):
        print("Rectangle area:", 10 * 5)
circle = Circle()
rectangle = Rectangle()
circle.area()
rectangle.area()

### Q11. Create Payment, UPI, and CardPayment with pay().
class Payment:
    def pay(self):
        print("Payment")
class UPI(Payment):
    def pay(self):
        print("Payment through UPI")
class CardPayment(Payment):
    def pay(self):
        print("Payment through Card")
upi = UPI()
card = CardPayment()
upi.pay()
card.pay()

### Q12. Create Employee subclasses with different calculate_salary() methods.
class Employee:
    def calculate_salary(self):
        print("Employee salary")
class Developer(Employee):
    def calculate_salary(self):
        print("Developer salary: 50000")
class Manager(Employee):
    def calculate_salary(self):
        print("Manager salary: 70000")
developer = Developer()
manager = Manager()
developer.calculate_salary()
manager.calculate_salary()

# Abstraction
### Q13. Create an abstract Vehicle class with start().
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car starts")
car = Car()
car.start()

### Q14. Create an abstract Shape class with area().
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        print("Circle area:", 3.14 * 5 * 5)
circle = Circle()
circle.area()

### Q15. Create an abstract Payment class with pay().
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(Payment):
    def pay(self):
        print("Payment through UPI")
upi = UPI()
upi.pay()

### Q16. Create an abstract Employee class with calculate_salary().
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Developer(Employee):
    def calculate_salary(self):
        print("Developer salary: 50000")
developer = Developer()
developer.calculate_salary()

### Q17. Create an abstract BankAccount class with withdraw().
from abc import ABC, abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        print("Withdrawn amount:", amount)
account = SavingsAccount()
account.withdraw(2000)

# Combined OOP
### Q18. Build a Student Management System using all four OOP pillars.
from abc import ABC, abstractmethod
class Person:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    def set_marks(self, marks):
        self.__marks = marks
class Result(Student, ABC):
    @abstractmethod
    def display_result(self):
        pass
class StudentResult(Result):
    def display_result(self):
        print("Name:", self.get_name())
        print("Marks:", self.get_marks())
student = StudentResult("Sneha", 85)
student.display_result()

### Q19. Build a Bank Management System.
from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
    def get_money(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    @abstractmethod
    def withdraw(self, amount):
        pass
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.get_money(amount):
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
account = SavingsAccount(10000)
account.deposit(2000)
account.withdraw(3000)
print("Balance:", account.get_balance())

### Q20. Build an Employee Management System.
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    def get_name(self):
        return self.__name
    def get_salary(self):
        return self.__salary
    @abstractmethod
    def calculate_salary(self):
        pass
class Developer(Employee):
    def calculate_salary(self):
        return self.get_salary() + 5000
class Manager(Employee):
    def calculate_salary(self):
        return self.get_salary() + 10000
developer = Developer("Amit", 40000)
manager = Manager("Rahul", 50000)
print(developer.get_name(), developer.calculate_salary())
print(manager.get_name(), manager.calculate_salary())

### Q21. Build a Vehicle Management System.
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand):
        self.__brand = brand
    def get_brand(self):
        return self.__brand
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print(self.get_brand(), "Car starts")
class Bike(Vehicle):
    def start(self):
        print(self.get_brand(), "Bike starts")
car = Car("Toyota")
bike = Bike("Honda")
car.start()
bike.start()

### Q22. Build a Library Management System.
from abc import ABC, abstractmethod
class LibraryItem(ABC):
    def __init__(self, title):
        self.__title = title
    def get_title(self):
        return self.__title
    @abstractmethod
    def display(self):
        pass
class Book(LibraryItem):
    def display(self):
        print("Book:", self.get_title())
class Magazine(LibraryItem):
    def display(self):
        print("Magazine:", self.get_title())
book = Book("Python Programming")
magazine = Magazine("Technology Today")
book.display()
magazine.display()

### Q23. Build an Online Food Ordering System using Encapsulation, Inheritance, Polymorphism, and Abstraction.
from abc import ABC, abstractmethod
class FoodItem(ABC):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    @abstractmethod
    def prepare(self):
        pass
class Pizza(FoodItem):
    def prepare(self):
        print("Preparing", self.get_name())
class Burger(FoodItem):
    def prepare(self):
        print("Preparing", self.get_name())
class Order:
    def __init__(self):
        self.__items = []
    def add_item(self, item):
        self.__items.append(item)
    def show_order(self):
        total = 0
        for item in self.__items:
            item.prepare()
            print(item.get_name(), "-", item.get_price())
            total += item.get_price()
        print("Total:", total)
order = Order()
pizza = Pizza("Cheese Pizza", 250)
burger = Burger("Veg Burger", 150)
order.add_item(pizza)
order.add_item(burger)
order.show_order()