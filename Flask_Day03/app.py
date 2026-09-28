# FLASK DAY 03
# Questions and Answers

from flask import Flask, request, render_template

app = Flask(__name__)


# Q1. What is request in Flask?
# Answer:
# request is used to get data sent by the user from the browser.

@app.route("/request")
def request_example():
    return "The request object is used to get user data."


# Q2. How do you get data from a URL?
# Answer:
# We can use request.args to get data from the URL.

@app.route("/user")
def user():
    name = request.args.get("name")
    return f"Hello {name}"


# Q3. How do you get form data in Flask?
# Answer:
# We use request.form to get data submitted through a form.

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        return f"Hello {name}"

    return """
    <form method="POST">
        <input type="text" name="name">
        <button type="submit">Submit</button>
    </form>
    """


# Q4. What is GET method?
# Answer:
# GET is used to request or retrieve data from the server.

@app.route("/get", methods=["GET"])
def get_method():
    return "This is a GET request."


# Q5. What is POST method?
# Answer:
# POST is used to send data to the server.

@app.route("/post", methods=["POST"])
def post_method():
    return "This is a POST request."


# Q6. What is render_template()?
# Answer:
# render_template() is used to display an HTML file.

@app.route("/home")
def home():
    return render_template("home.html")


# Q7. How do you pass data from Flask to HTML?
# Answer:
# We pass data as a variable inside render_template().

@app.route("/profile")
def profile():
    name = "Sneha"
    return render_template("profile.html", name=name)


# Q8. How can HTML display Flask data?
# Answer:
# HTML uses Jinja2 syntax {{ variable }}.

# Example:
# <h1>Hello {{ name }}</h1>


# Q9. What is Jinja2?
# Answer:
# Jinja2 is a template engine used by Flask to create dynamic HTML pages.

@app.route("/jinja")
def jinja():
    name = "Sneha"
    age = 21

    return render_template(
        "profile.html",
        name=name,
        age=age
    )


# Q10. How do you use if condition in Jinja2?
# Answer:
# We use {% if %} and {% endif %}.

# Example:
# {% if age >= 18 %}
#     <p>You are an adult.</p>
# {% endif %}


# Q11. How do you use a for loop in Jinja2?
# Answer:
# We use {% for %} and {% endfor %}.

# Example:
# {% for name in names %}
#     <p>{{ name }}</p>
# {% endfor %}


# Q12. How do you pass a list from Flask to HTML?
# Answer:

@app.route("/students")
def students():
    students = ["Sneha", "Rahul", "Priya", "Amit"]

    return render_template(
        "students.html",
        students=students
    )


# Q13. What is the purpose of methods in @app.route()?
# Answer:
# It tells Flask which HTTP methods the route accepts.

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Login submitted"

    return "Login page"


# Q14. How do you get multiple form fields?
# Answer:
# Use request.form.get() for each field.

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        return f"""
        Name: {name}<br>
        Email: {email}<br>
        Password: {password}
        """

    return """
    <form method="POST">

        <input type="text" name="name" placeholder="Enter Name">
        <br><br>

        <input type="email" name="email" placeholder="Enter Email">
        <br><br>

        <input type="password" name="password" placeholder="Enter Password">
        <br><br>

        <button type="submit">Register</button>

    </form>
    """


# Q15. What is request.method?
# Answer:
# request.method tells us which HTTP method was used.

@app.route("/method", methods=["GET", "POST"])
def method_example():

    if request.method == "GET":
        return "GET method"

    if request.method == "POST":
        return "POST method"


# Q16. What is a template folder?
# Answer:
# templates folder stores HTML files used by Flask.

# Project structure:
#
# project/
# │
# ├── app.py
# │
# └── templates/
#     ├── home.html
#     ├── profile.html
#     └── students.html


# Q17. What is static folder?
# Answer:
# static folder stores CSS, JavaScript and image files.

# Project structure:
#
# project/
# │
# ├── app.py
# │
# ├── templates/
# │   └── home.html
# │
# └── static/
#     ├── style.css
#     └── script.js


# Q18. How do you connect CSS with Flask HTML?
# Answer:
# Use url_for() inside the HTML file.

# Example:
# <link rel="stylesheet"
#       href="{{ url_for('static', filename='style.css') }}">


# Q19. What is url_for()?
# Answer:
# url_for() generates URLs for Flask routes and static files.

@app.route("/about")
def about():
    return "About Page"


# Example in HTML:
# <a href="{{ url_for('about') }}">About</a>


# Q20. What is the basic Flask project flow?
# Answer:
#
# Browser
#    ↓
# Flask Route
#    ↓
# Python Function
#    ↓
# Processing
#    ↓
# HTML Template
#    ↓
# Browser


if __name__ == "__main__":
    app.run(debug=True)