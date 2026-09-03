import student
import result
import validation


while True:

    print("\n==============================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("==============================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Result")
    print("5. Delete Student")
    print("6. Exit")


    choice = input("Enter choice: ")


    # ADD STUDENT
    if choice == "1":

        roll_no = input(
            "Enter Roll Number: "
        )


        if not validation.valid_roll_no(roll_no):

            print("Invalid Roll Number.")

            continue


        name = input(
            "Enter Student Name: "
        )


        if not validation.valid_name(name):

            print("Invalid Name.")

            continue


        marks = input(
            "Enter Marks: "
        )


        if not validation.valid_marks(marks):

            print("Invalid Marks.")

            continue


        student.add_student(
            roll_no,
            name,
            marks
        )


        print(
            "Student added successfully."
        )


    # VIEW STUDENTS
    elif choice == "2":

        student.view_students()


    # SEARCH STUDENT
    elif choice == "3":

        roll_no = input(
            "Enter Roll Number: "
        )


        found = student.search_student(
            roll_no
        )


        if found:

            print("\nStudent Found")

            print(
                "Roll No:",
                found[0]
            )

            print(
                "Name:",
                found[1]
            )

            print(
                "Marks:",
                found[2]
            )


        else:

            print(
                "Student not found."
            )


    # CALCULATE RESULT
    elif choice == "4":

        roll_no = input(
            "Enter Roll Number: "
        )


        found = student.search_student(
            roll_no
        )


        if found:

            marks = float(found[2])


            percentage = (
                result.calculate_percentage(
                    marks
                )
            )


            grade = (
                result.calculate_grade(
                    percentage
                )
            )


            print("\n--- RESULT ---")


            print(
                "Name:",
                found[1]
            )


            print(
                "Percentage:",
                percentage
            )


            print(
                "Grade:",
                grade
            )


        else:

            print(
                "Student not found."
            )


    # DELETE STUDENT
    elif choice == "5":

        roll_no = input(
            "Enter Roll Number: "
        )


        deleted = student.delete_student(
            roll_no
        )


        if deleted:

            print(
                "Student deleted successfully."
            )

        else:

            print(
                "Student not found."
            )


    # EXIT
    elif choice == "6":

        print("Thank you!")

        break


    else:

        print("Invalid choice.")