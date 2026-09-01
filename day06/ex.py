# Q1. Create a tuple and print it.
fruits = ("apple", "banana", "mango")
print(fruits)

# Q2. Print the first item from the tuple.
fruits = ("apple", "banana", "mango")
print(fruits[0])

# Q3. Print the last item from the tuple.
fruits = ("apple", "banana", "mango")
print(fruits[-1])

# Q4. Create a tuple with different types of values and print it.
student = ("Sneha", 20, 77.5)
print(student)

# Q5. Create a set and print it.
numbers = {1, 2, 3, 4, 5}
print(numbers)

# Q6. Create a set with duplicate values and print it.
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)

# Q7. Add an item to a set.
fruits = {"apple", "banana"}
fruits.add("mango")
print(fruits)

# Q8. Remove an item from a set.
fruits = {"apple", "banana", "mango"}
fruits.remove("banana")
print(fruits)

# Q9. Find the union of two sets.
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)

# Q10. Find the common items in two sets.
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)

# Q11. Create a dictionary and print it.
student = {
    "name": "Sneha",
    "age": 20,
    "city": "Pune"
}
print(student)

# Q12. Print a value from a dictionary.
student = {
    "name": "Sneha",
    "age": 20
}
print(student["name"])

# Q13. Add a new item to a dictionary.
student = {
    "name": "Sneha",
    "age": 20
}
student["course"] = "MCA"
print(student)

# Q14. Change a value in a dictionary.
student = {
    "name": "Sneha",
    "age": 20
}
student["age"] = 21
print(student)

# Q15. Print all keys and values from a dictionary.
student = {
    "name": "Sneha",
    "age": 20,
    "city": "Pune"
}
for key, value in student.items():
    print(key, value)