import date_utils


print(
    "Current Date:",
    date_utils.current_date()
)


print(
    "Current Time:",
    date_utils.current_time()
)


birth_year = int(
    input("Enter birth year: ")
)


print(
    "Approximate Age:",
    date_utils.calculate_age(birth_year)
)


date1 = input(
    "Enter first date (DD-MM-YYYY): "
)


date2 = input(
    "Enter second date (DD-MM-YYYY): "
)


print(
    "Days Between:",
    date_utils.days_between_dates(
        date1,
        date2
    )
)