from datetime import datetime

future_date = input("Enter future date (DD-MM-YYYY): ")

future = datetime.strptime(future_date, "%d-%m-%Y")

today = datetime.now()

remaining = future - today

print("Days remaining:", remaining.days)