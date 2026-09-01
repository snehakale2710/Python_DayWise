# Create a tuple containing five numbers
numbers = (10, 20, 30, 40, 50)
print(numbers)

# Print the first and last element
print(numbers[0])
print(numbers[-1])

# Find the length of a tuple
print(len(numbers))

# Count a particular value
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))

# Find the index of a value
numbers = (10, 20, 30, 40, 50)
print(numbers.index(30))

# Unpack a tuple into variables
numbers = (10, 20, 30)
a, b, c = numbers
print(a)
print(b)
print(c)

# Create a student information tuple
student = ("Sneha", 20, "MCA", 77)
print(student)

# Create a set of five numbers
numbers = {10, 20, 30, 40, 50}
print(numbers)

# Add an element to a set
numbers = {10, 20, 30}
numbers.add(40)
print(numbers)

# Remove an element
numbers = {10, 20, 30, 40}
numbers.remove(30)
print(numbers)

# Remove duplicate values from a list using a set
numbers = [10, 20, 10, 30, 20, 40]
numbers = set(numbers)
print(numbers)

# Find union of two sets
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)

# Find intersection of two sets
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)

# Find difference between two sets
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)

# Create a student dictionary
student = {
    "name": "Sneha",
    "age": 20,
    "course": "MCA"
}
print(student)

# Access values using keys
print(student["name"])
print(student["age"])

# Add a new key
student["city"] = "Pune"
print(student)

# Update an existing value
student["age"] = 21
print(student)

# Delete a key
del student["city"]
print(student)

# Use keys(), values() and items()
print(student.keys())
print(student.values())
print(student.items())

# Check whether a key exists
if "name" in student:
    print("Name is present")

# Create a dictionary containing student marks
marks = {
    "Math": 85,
    "English": 78,
    "Computer": 90
}
print(marks)

# Create a list of dictionaries for five students
students = [
    {"name": "Sneha", "marks": 85},
    {"name": "Rahul", "marks": 72},
    {"name": "Priya", "marks": 90},
    {"name": "Amit", "marks": 68},
    {"name": "Neha", "marks": 80}
]
print(students)

# Display students whose marks are greater than 75
for student in students:
    if student["marks"] > 75:
        print(student["name"])