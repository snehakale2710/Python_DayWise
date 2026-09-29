from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/profile/<name>")
def profile(name):
    return render_template("index.html", name=name)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        return render_template(
            "index.html",
            username=username,
            password=password
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)