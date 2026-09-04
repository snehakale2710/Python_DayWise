# Q1. Create a file named demo.txt and write "Hello Python" into it.
f = open("demo.txt", "w")
f.write("Hello Python")
f.close()

# Q2. Create a file named student.txt and write your name, age, and city into it.
f = open("student.txt", "w")
f.write("Name: Sneha\n")
f.write("Age: 20\n")
f.write("City: Pune")
f.close()

# Q3. Read and display the complete contents of demo.txt.
f = open("demo.txt", "r")
print(f.read())
f.close()

# Q4. Create a file and write 5 different messages into it.
f = open("messages.txt", "w")
f.write("Hello\n")
f.write("Good Morning\n")
f.write("Welcome\n")
f.write("Good Day\n")
f.write("Learn Python")
f.close()

# Q5. Read a file line by line and print each line.
f = open("messages.txt", "r")
for line in f:
    print(line)
f.close()

# Q6. Count the number of lines present in a text file.
f = open("messages.txt", "r")
count = 0
for line in f:
    count = count + 1
print("Number of lines =", count)
f.close()

# Q7. Count the number of words present in a text file.
f = open("messages.txt", "r")
data = f.read()
words = data.split()
print("Number of words =", len(words))
f.close()

# Q8. Count the number of characters present in a text file.
f = open("messages.txt", "r")
data = f.read()
print("Number of characters =", len(data))
f.close()

# Q9. Check whether a particular word exists in a file.
word = input("Enter word to search: ")
f = open("messages.txt", "r")
data = f.read()
if word in data:
    print("Word exists in file")
else:
    print("Word does not exist in file")
f.close()

# Q10. Read a file and display only those lines that contain the word "Python".
f = open("messages.txt", "r")
for line in f:
    if "Python" in line:
        print(line)
f.close()

# Q11. Create students.txt and store the names of 5 students.
f = open("students.txt", "w")
f.write("Sneha\n")
f.write("Rahul\n")
f.write("Priya\n")
f.write("Amit\n")
f.write("Neha\n")
f.close()

# Q12. Add a new student name to the existing students.txt file without deleting old data.
f = open("students.txt", "a")
f.write("Riya\n")
f.close()

# Q13. Create a file numbers.txt and store numbers from 1 to 10.
f = open("numbers.txt", "w")
for i in range(1, 11):
    f.write(str(i) + "\n")
f.close()

# Q14. Append numbers from 11 to 20 to the same file.
f = open("numbers.txt", "a")
for i in range(11, 21):
    f.write(str(i) + "\n")
f.close()

# Q15. Create a file cities.txt and store 5 city names. Then append 3 more cities.
f = open("cities.txt", "w")
f.write("Pune\n")
f.write("Mumbai\n")
f.write("Delhi\n")
f.write("Nagpur\n")
f.write("Nashik\n")
f.close()
f = open("cities.txt", "a")
f.write("Chennai\n")
f.write("Kolkata\n")
f.write("Bangalore\n")
f.close()

# Q16. Take student name and marks from the user and store them in a file.
name = input("Enter student name: ")
marks = input("Enter marks: ")
f = open("student_marks.txt", "w")
f.write("Name: " + name + "\n")
f.write("Marks: " + marks)
f.close()

# Q17. Take 5 employee names from the user and store them in employees.txt.
f = open("employees.txt", "w")
for i in range(5):
    name = input("Enter employee name: ")
    f.write(name + "\n")
f.close()

# Q18. Take 5 numbers from the user and store them in numbers.txt.
f = open("numbers_user.txt", "w")
for i in range(5):
    num = input("Enter number: ")
    f.write(num + "\n")
f.close()

# Q19. Create a class Student and create one object of it.
class Student:
    pass
s1 = Student()
print("Student object created")

# Q20. Create a class Student with attributes name, age, and city.
class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

# Q21. Create an object and display all values.
s1 = Student("Sneha", 20, "Pune")
print("Name =", s1.name)
print("Age =", s1.age)
print("City =", s1.city)

# Q22. Create a class Employee with name, salary, and department.
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
e1 = Employee("Rahul", 30000, "IT")
print("Name =", e1.name)
print("Salary =", e1.salary)
print("Department =", e1.department)

# Q23. Create a class Car with brand, model, and price.
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
c1 = Car("Toyota", "Fortuner", 4000000)
print("Brand =", c1.brand)
print("Model =", c1.model)
print("Price =", c1.price)

# Q24. Create a class Mobile with company, model, and price. Create 3 objects.
class Mobile:
    def __init__(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price
m1 = Mobile("Samsung", "S24", 70000)
m2 = Mobile("Apple", "iPhone 15", 70000)
m3 = Mobile("OnePlus", "12", 60000)
print(m1.company, m1.model, m1.price)
print(m2.company, m2.model, m2.price)
print(m3.company, m3.model, m3.price)

# Q25. Create a class Book with title, author, and price. Create two objects.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
b1 = Book("Python", "John", 500)
b2 = Book("Java", "Robert", 600)
print(b1.title, b1.author, b1.price)
print(b2.title, b2.author, b2.price)

# Q26. Create a class Product with product name, price, and quantity.
class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
p1 = Product("Laptop", 50000, 2)
print("Product Name =", p1.product_name)
print("Price =", p1.price)
print("Quantity =", p1.quantity)

# Q27. Create a class Employee and create 5 employee objects.
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
e1 = Employee("Rahul", 30000, "IT")
e2 = Employee("Priya", 35000, "HR")
e3 = Employee("Amit", 40000, "Finance")
e4 = Employee("Neha", 32000, "Marketing")
e5 = Employee("Riya", 38000, "IT")
print(e1.name, e1.salary, e1.department)
print(e2.name, e2.salary, e2.department)
print(e3.name, e3.salary, e3.department)
print(e4.name, e4.salary, e4.department)
print(e5.name, e5.salary, e5.department)

# Q28. Create a class Laptop and store brand, RAM, processor, and price.
class Laptop:
    def __init__(self, brand, RAM, processor, price):
        self.brand = brand
        self.RAM = RAM
        self.processor = processor
        self.price = price
l1 = Laptop("Lenovo", "16GB", "Intel i7", 65000)
print("Brand =", l1.brand)
print("RAM =", l1.RAM)
print("Processor =", l1.processor)
print("Price =", l1.price)

# Q29. Create a class BankAccount with account holder name, account number, and balance.
class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
a1 = BankAccount("Sneha", "1234567890", 25000)
print("Account Holder =", a1.name)
print("Account Number =", a1.account_number)
print("Balance =", a1.balance)