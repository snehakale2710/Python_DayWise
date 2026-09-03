def valid_roll_no(roll_no):

    return roll_no.isdigit()


def valid_name(name):

    return name.replace(" ", "").isalpha()


def valid_marks(marks):

    try:

        marks = float(marks)

        return 0 <= marks <= 100

    except ValueError:

        return False