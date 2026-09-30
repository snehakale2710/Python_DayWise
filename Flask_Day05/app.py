from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "Python Basics", "author": "John", "price": 500},
    {"id": 2, "title": "Flask Guide", "author": "David", "price": 600}
]

students = [
    {"name": "Sneha", "marks": 85, "status": "Pass"},
    {"name": "Rahul", "marks": 35, "status": "Fail"}
]

employees = [
    {"id": 1, "name": "Amit", "department": "IT", "salary": 40000},
    {"id": 2, "name": "Priya", "department": "HR", "salary": 35000}
]

cart = []


# Question 1: Book Management API

@app.route("/api/books", methods=["GET"])
def get_books():
    return jsonify(books), 200


@app.route("/api/books", methods=["POST"])
def add_book():
    data = request.get_json()

    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"],
        "price": data["price"]
    }

    books.append(new_book)

    return jsonify(new_book), 201


# Question 2: Student Grade Checker API

@app.route("/api/students", methods=["GET"])
def get_students():
    return jsonify(students), 200


@app.route("/api/students", methods=["POST"])
def add_student():
    data = request.get_json()

    marks = data["marks"]

    if marks >= 40:
        status = "Pass"
    else:
        status = "Fail"

    student = {
        "name": data["name"],
        "marks": marks,
        "status": status
    }

    students.append(student)

    return jsonify(student), 201


# Question 3: Employee Directory API

@app.route("/api/employees", methods=["GET"])
def get_employees():
    return jsonify(employees), 200


@app.route("/api/employees", methods=["POST"])
def add_employee():
    data = request.get_json()

    employee = {
        "id": len(employees) + 1,
        "name": data["name"],
        "department": data["department"],
        "salary": data["salary"]
    }

    employees.append(employee)

    return jsonify(employee), 201


@app.route("/api/employees/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    for employee in employees:
        if employee["id"] == emp_id:
            employees.remove(employee)
            return jsonify({"message": "Employee deleted successfully"}), 200

    return jsonify({"message": "Employee not found"}), 404


# Question 4: Shopping Cart API with Validation

@app.route("/api/cart", methods=["POST"])
def add_to_cart():
    data = request.get_json()

    product_name = data["product_name"]
    price = data["price"]

    if price <= 0:
        return jsonify({"message": "Invalid price"}), 400

    item = {
        "product_name": product_name,
        "price": price
    }

    cart.append(item)

    return jsonify({
        "message": "Product added to cart successfully",
        "item": item
    }), 201


if __name__ == "__main__":
    app.run(debug=True)