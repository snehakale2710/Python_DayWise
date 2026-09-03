from datetime import datetime


def current_date():

    return datetime.now().strftime("%d-%m-%Y")


def current_time():

    return datetime.now().strftime("%H:%M:%S")


def calculate_age(birth_year):

    current_year = datetime.now().year

    return current_year - birth_year


def days_between_dates(date1, date2):

    d1 = datetime.strptime(
        date1,
        "%d-%m-%Y"
    )

    d2 = datetime.strptime(
        date2,
        "%d-%m-%Y"
    )

    return abs((d2 - d1).days)