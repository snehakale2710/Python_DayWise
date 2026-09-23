# Q1. Create a class Student with name and age attributes and display them.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Sneha", 21)
print(student.name)
print(student.age)


# Q2. Create a class Employee with a method to display employee details.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

employee = Employee("Rahul", 30000)
employee.display()


# Q3. Create a class Calculator with methods for addition and subtraction.

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

c = Calculator()
print(c.add(10, 5))
print(c.subtract(10, 5))


# Q4. Create a class Rectangle to calculate area.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r = Rectangle(10, 5)
print("Area:", r.area())


# Q5. Create a class Circle to calculate area.

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * self.radius * self.radius

c = Circle(5)
print("Area:", c.area())


# Q6. Create a class BankAccount with deposit and withdraw methods.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display(self):
        print("Balance:", self.balance)

account = BankAccount(10000)
account.deposit(5000)
account.withdraw(2000)
account.display()


# Q7. Create a class Car with a method to start the car.

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "car started")

car = Car("Toyota")
car.start()


# Q8. Create a class Person and use __str__() to display details.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

person = Person("Sneha", 21)
print(person)


# Q9. Create a class Product with a class variable company.

class Product:
    company = "ABC Company"

    def __init__(self, name, price):
        self.name = name
        self.price = price

product = Product("Laptop", 50000)
print(product.name)
print(product.price)
print(Product.company)


# Q10. Create a class Student with a class method to display the college name.

class Student:
    college = "Greenfingers College"

    @classmethod
    def display_college(cls):
        print("College:", cls.college)

Student.display_college()


# Q11. Create a class Math with a static method to find the square of a number.

class Math:
    @staticmethod
    def square(number):
        return number * number

print(Math.square(6))


# Q12. Create a parent class Animal and child class Dog using inheritance.

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog = Dog()
dog.eat()
dog.bark()


# Q13. Create a parent class Vehicle and child class Bike using inheritance.

class Vehicle:
    def start(self):
        print("Vehicle started")

class Bike(Vehicle):
    def ride(self):
        print("Bike is running")

bike = Bike()
bike.start()
bike.ride()


# Q14. Demonstrate method overriding using Animal and Dog classes.

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

animal = Animal()
dog = Dog()

animal.sound()
dog.sound()


# Q15. Demonstrate multilevel inheritance.

class Grandparent:
    def show_grandparent(self):
        print("Grandparent class")

class Parent(Grandparent):
    def show_parent(self):
        print("Parent class")

class Child(Parent):
    def show_child(self):
        print("Child class")

child = Child()
child.show_grandparent()
child.show_parent()
child.show_child()


# Q16. Demonstrate multiple inheritance.

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


# Q17. Create an abstract class Shape with an abstract method area.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

square = Square(5)
print("Area:", square.area())


# Q18. Demonstrate polymorphism using different classes.

class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)


# Q19. Create a class with private variable and access it using a method.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

student = Student("Sneha", 85)
print("Name:", student.name)
print("Marks:", student.get_marks())


# Q20. Create a class Employee using encapsulation with getter and setter methods.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

employee = Employee("Sneha", 30000)

print("Name:", employee.name)
print("Salary:", employee.get_salary())

employee.set_salary(40000)

print("Updated Salary:", employee.get_salary())