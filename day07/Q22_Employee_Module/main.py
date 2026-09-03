from employee import employee_details
from employee import calculate_salary


name = input("Enter employee name: ")

employee_id = input("Enter employee ID: ")

department = input("Enter department: ")

basic = float(input("Enter basic salary: "))

allowance = float(input("Enter allowance: "))

bonus = float(input("Enter bonus: "))


print("\n--- Employee Details ---")

employee_details(name, employee_id, department)

salary = calculate_salary(basic, allowance, bonus)

print("Total Salary:", salary)