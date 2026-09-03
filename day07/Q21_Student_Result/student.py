def calculate_total(marks):
    return sum(marks)


def calculate_percentage(marks):
    total = calculate_total(marks)
    return total / len(marks)


def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"