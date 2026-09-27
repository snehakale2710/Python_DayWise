from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


# ============================================================
# FLASK DAY 01
# ============================================================

# Q1. Hello World Route
@app.route("/")
def home():
    app_name = "My First Flask App"

    questions = [
        {"number": 1, "title": "Hello World Route", "url": "/"},
        {"number": 2, "title": "User Profile Greeting", "url": "/greet/Sneha"},
        {"number": 3, "title": "Age Check", "url": "/age"},
        {"number": 4, "title": "Current Year Footer", "url": "/year"},
        {"number": 5, "title": "Score Card", "url": "/score"},
        {"number": 6, "title": "Product Detail Route", "url": "/product/101"},
        {"number": 7, "title": "Voter Eligibility Check", "url": "/voter"},
        {"number": 8, "title": "Admin Dashboard Access", "url": "/admin"},
        {"number": 9, "title": "Pass / Fail Logic", "url": "/marks"},
        {"number": 10, "title": "Stock Availability", "url": "/stock"},
        {"number": 11, "title": "Odd or Even Identifier", "url": "/number"},
        {"number": 12, "title": "Login Banner", "url": "/login"},
        {"number": 13, "title": "Fruits List Rendering", "url": "/fruits"},
        {"number": 14, "title": "Numbered Student List", "url": "/students"},
        {"number": 15, "title": "Product Table", "url": "/products"},
        {"number": 16, "title": "Empty List Fallback", "url": "/items"},
        {"number": 17, "title": "Loop Index Tracker", "url": "/tasks"},
        {"number": 18, "title": "Filter Even Numbers", "url": "/even"},
        {"number": 19, "title": "User Bio Card", "url": "/profile"},
        {"number": 20, "title": "Student Grade Card", "url": "/grades"},
        {"number": 21, "title": "Blog Posts Feed", "url": "/blog"},
        {"number": 22, "title": "Calculate Total Price", "url": "/cart"},
        {"number": 23, "title": "High Score Highlight", "url": "/players"},
        {"number": 24, "title": "Multi-Category Directory", "url": "/directory"}
    ]

    return render_template(
        "index.html",
        app_name=app_name,
        questions=questions
    )


# Q2. User Profile Greeting
@app.route("/greet/<username>")
def greet(username):
    return render_template("greet.html", username=username)


# Q3. Age Check
@app.route("/age")
def age():
    age = 20
    return render_template("age.html", age=age)


# Q4. Current Year Footer
@app.route("/year")
def year():
    current_year = datetime.now().year
    return render_template("year.html", current_year=current_year)


# Q5. Score Card
@app.route("/score")
def score():
    name = "Sneha"
    score = 85
    return render_template("score.html", name=name, score=score)


# Q6. Product Detail Route
@app.route("/product/<int:id>")
def product(id):
    return render_template("product.html", id=id)


# Q7. Voter Eligibility Check
@app.route("/voter")
def voter():
    age = 19
    return render_template("voter.html", age=age)


# Q8. Admin Dashboard Access
@app.route("/admin")
def admin():
    user = {
        "name": "John",
        "role": "admin"
    }

    return render_template("admin.html", user=user)


# Q9. Pass / Fail Logic
@app.route("/marks")
def marks():
    marks = [35, 45, 60, 30, 80]
    return render_template("marks.html", marks=marks)


# Q10. Stock Availability
@app.route("/stock")
def stock():
    stock_count = 0
    return render_template("stock.html", stock_count=stock_count)


# Q11. Odd or Even Identifier
@app.route("/number")
def number():
    n = 10
    return render_template("number.html", n=n)


# Q12. Login Banner
@app.route("/login")
def login():
    is_logged_in = True
    return render_template("login.html", is_logged_in=is_logged_in)


# Q13. Fruits List Rendering
@app.route("/fruits")
def fruits():
    fruits = ["Apple", "Banana", "Cherry"]
    return render_template("fruits.html", fruits=fruits)


# Q14. Numbered Student List
@app.route("/students")
def students():
    students = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Emma"
    ]

    return render_template("students.html", students=students)


# Q15. Product Table
@app.route("/products")
def products():
    products = [
        {"name": "Laptop", "price": 999},
        {"name": "Phone", "price": 499}
    ]

    return render_template("products.html", products=products)


# Q16. Empty List Fallback
@app.route("/items")
def items():
    items = []
    return render_template("items.html", items=items)


# Q17. Loop Index Tracker
@app.route("/tasks")
def tasks():
    tasks = [
        "Task One",
        "Task Two",
        "Task Three",
        "Task Four",
        "Task Five"
    ]

    return render_template("tasks.html", tasks=tasks)


# Q18. Filter Even Numbers
@app.route("/even")
def even():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    return render_template(
        "even.html",
        numbers=numbers
    )


# Q19. User Bio Card
@app.route("/profile")
def profile():
    profile = {
        "name": "Alice",
        "city": "NYC",
        "skills": ["Python", "Flask", "SQL"]
    }

    return render_template(
        "profile.html",
        profile=profile
    )


# Q20. Student Grade Card
@app.route("/grades")
def grades():
    scores = [
        {"subject": "Math", "marks": 88},
        {"subject": "Science", "marks": 92}
    ]

    return render_template(
        "grades.html",
        scores=scores
    )


# Q21. Blog Posts Feed
@app.route("/blog")
def blog():
    posts = [
        {
            "title": "Flask Day 1",
            "author": "Sam",
            "views": 150
        }
    ]

    return render_template(
        "blog.html",
        posts=posts
    )


# Q22. Calculate Total Price
@app.route("/cart")
def cart():
    cart_items = {
        "Book": 15,
        "Pen": 3
    }

    total = sum(cart_items.values())

    return render_template(
        "cart.html",
        cart_items=cart_items,
        total=total
    )


# Q23. High Score Highlight
@app.route("/players")
def players():
    players = [
        {"name": "John", "score": 95},
        {"name": "Alice", "score": 85},
        {"name": "Sam", "score": 92}
    ]

    return render_template(
        "players.html",
        players=players
    )


# Q24. Multi-Category Directory
@app.route("/directory")
def directory():
    directory = {
        "Frontend": ["HTML", "CSS"],
        "Backend": ["Python", "Flask"]
    }

    return render_template(
        "directory.html",
        directory=directory
    )


if __name__ == "__main__":
    app.run(debug=True)