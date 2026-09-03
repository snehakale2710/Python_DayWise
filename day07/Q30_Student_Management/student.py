FILE_NAME = "data.txt"


def add_student(roll_no, name, marks):

    with open(FILE_NAME, "a") as file:

        file.write(
            f"{roll_no},{name},{marks}\n"
        )


def view_students():

    try:

        with open(FILE_NAME, "r") as file:

            students = file.readlines()


        if not students:

            print("No students found.")

            return


        print("\n--- Students ---")


        for student in students:

            roll_no, name, marks = (
                student.strip().split(",")
            )

            print(
                "Roll No:",
                roll_no,
                "| Name:",
                name,
                "| Marks:",
                marks
            )


    except FileNotFoundError:

        print("No student data found.")


def search_student(roll_no):

    try:

        with open(FILE_NAME, "r") as file:

            for student in file:

                data = student.strip().split(",")

                if data[0] == roll_no:

                    return data


        return None


    except FileNotFoundError:

        return None


def delete_student(roll_no):

    try:

        with open(FILE_NAME, "r") as file:

            students = file.readlines()


        found = False


        with open(FILE_NAME, "w") as file:

            for student in students:

                data = student.strip().split(",")


                if data[0] != roll_no:

                    file.write(student)

                else:

                    found = True


        return found


    except FileNotFoundError:

        return False