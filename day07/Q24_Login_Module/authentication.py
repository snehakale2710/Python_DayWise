users = {}


def register_user(username, password):

    if username in users:

        return "Username already exists."

    users[username] = password

    return "Registration successful."


def login_user(username, password):

    if username in users and users[username] == password:

        return "Login successful."

    return "Invalid username or password."