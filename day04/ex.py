# 1. Take a name from the user and print it in uppercase.
name = input("Enter your name: ")
print(name.upper())

# 2. Take a name from the user and print it in lowercase.
name = input("Enter your name: ")
print(name.lower())

# 3. Take a full name and print it in title case.
name = input("Enter your full name: ")
print(name.title())

# 4. Find the length of a string entered by the user.
text = input("Enter a string: ")
print(len(text))

# 5. Print the first character of a string.
text = input("Enter a string: ")
print(text[0])

# 6. Print the last character of a string.
text = input("Enter a string: ")
print(text[-1])

# 7. Print the first three characters of a string using slicing.
text = input("Enter a string: ")
print(text[:3])

# 8. Reverse a string using slicing.
text = input("Enter a string: ")
print(text[::-1])

# 9. Count how many times the letter 'a' appears in a string.
text = input("Enter a string: ")
print(text.lower().count("a"))

# 10. Replace the word 'Python' with 'Java' in a sentence.
sentence = input("Enter a sentence: ")
print(sentence.replace("Python", "Java"))

# 11. Remove extra spaces from the beginning and end of a string.
text = input("Enter a string: ")
print(text.strip())

# 12. Check whether a given word exists inside a sentence.
sentence = input("Enter a sentence: ")
word = input("Enter a word: ")
print(word in sentence)

# 13. Take first name and last name and create a full name.
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
full_name = first_name + " " + last_name
print(full_name)

# 14. Use an f-string to display a student's name, age and city.
name = input("Enter student name: ")
age = input("Enter age: ")
city = input("Enter city: ")
print(f"Name: {name}, Age: {age}, City: {city}")

# 15. Check whether a string is empty or not.
text = input("Enter a string: ")
if text == "":
    print("String is empty")
else:
    print("String is not empty")

# 16. Check whether a string starts with a specific letter.
text = input("Enter a string: ")
letter = input("Enter a letter: ")
print(text.startswith(letter))

# 17. Check whether a string ends with '.com'.
text = input("Enter a string: ")
print(text.endswith(".com"))

# 18. Count the number of vowels in a string.
text = input("Enter a string: ")
count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print(count)

# 19. Count the number of words in a sentence.
sentence = input("Enter a sentence: ")
words = sentence.split()
print(len(words))

# 20. Create a program that takes an email address and displays the username part before '@'.
email = input("Enter your email address: ")
username = email.split("@")[0]
print(username)