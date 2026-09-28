# FLASK DAY 02 ASSIGNMENT
# Question + Answer in One File

from flask import Flask, request

app = Flask(__name__)


# Q1. Create a basic Flask application.
# Answer:
@app.route("/")
def home():
    return "Welcome to Flask Day 02"


# Q2. Create a route that displays your name.
# Answer:
@app.route("/name")
def name():
    return "My name is Sneha"


# Q3. Create a route that displays a welcome message.
# Answer:
@app.route("/welcome")
def welcome():
    return "Welcome to Flask Application"


# Q4. Create a route that displays an HTML heading.
# Answer:
@app.route("/heading")
def heading():
    return "<h1>Flask Day 02</h1>"


# Q5. Create a route that displays multiple HTML elements.
# Answer:
@app.route("/html")
def html():
    return """
    <h1>Flask Application</h1>
    <p>This is my Day 02 assignment.</p>
    <b>Learning Flask</b>
    """


# Q6. Create a route using a variable in the URL.
# Answer:
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"


# Q7. Create a route that accepts an integer value.
# Answer:
@app.route("/number/<int:num>")
def number(num):
    return f"The number is {num}"


# Q8. Create a route to calculate the square of a number.
# Answer:
@app.route("/square/<int:num>")
def square(num):
    return f"Square of {num} is {num * num}"


# Q9. Create a route to calculate the cube of a number.
# Answer:
@app.route("/cube/<int:num>")
def cube(num):
    return f"Cube of {num} is {num * num * num}"


# Q10. Create a route that accepts two numbers and adds them.
# Answer:
@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"Addition = {a + b}"


# Q11. Create a route that subtracts two numbers.
# Answer:
@app.route("/subtract/<int:a>/<int:b>")
def subtract(a, b):
    return f"Subtraction = {a - b}"


# Q12. Create a route that multiplies two numbers.
# Answer:
@app.route("/multiply/<int:a>/<int:b>")
def multiply(a, b):
    return f"Multiplication = {a * b}"


# Q13. Create a route that divides two numbers.
# Answer:
@app.route("/divide/<int:a>/<int:b>")
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return f"Division = {a / b}"


# Q14. Get data using query parameters.
# Example: /search?name=Sneha
# Answer:
@app.route("/search")
def search():
    name = request.args.get("name")
    return f"Search result for: {name}"


# Q15. Get two values using query parameters.
# Example: /details?name=Sneha&age=21
# Answer:
@app.route("/details")
def details():
    name = request.args.get("name")
    age = request.args.get("age")

    return f"Name: {name}<br>Age: {age}"


# Q16. Create a route to check whether a number is even or odd.
# Answer:
@app.route("/evenodd/<int:num>")
def even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even"
    else:
        return f"{num} is Odd"


# Q17. Create a route to check whether a number is positive, negative or zero.
# Answer:
@app.route("/check/<int:num>")
def check_number(num):
    if num > 0:
        return f"{num} is Positive"
    elif num < 0:
        return f"{num} is Negative"
    else:
        return "The number is Zero"


# Q18. Create a route to calculate the area of a rectangle.
# Answer:
@app.route("/rectangle/<int:length>/<int:width>")
def rectangle(length, width):
    area = length * width
    return f"Area of Rectangle = {area}"


# Q19. Create a route to calculate the area of a circle.
# Answer:
@app.route("/circle/<float:radius>")
def circle(radius):
    area = 3.14 * radius * radius
    return f"Area of Circle = {area}"


# Q20. Create a route that displays a list of students.
# Answer:
@app.route("/students")
def students():
    students = ["Sneha", "Rahul", "Priya", "Amit"]

    return "<h2>Students</h2>" + "<br>".join(students)


# Run Flask application
if __name__ == "__main__":
    app.run(debug=True)