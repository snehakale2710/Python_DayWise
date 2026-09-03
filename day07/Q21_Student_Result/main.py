from student import calculate_total
from student import calculate_percentage
from student import calculate_grade


marks = []

for i in range(5):

    mark = float(input(f"Enter marks for subject {i + 1}: "))

    marks.append(mark)


total = calculate_total(marks)

percentage = calculate_percentage(marks)

grade = calculate_grade(percentage)


print("\n--- RESULT ---")

print("Total =", total)

print("Percentage =", percentage)

print("Grade =", grade)