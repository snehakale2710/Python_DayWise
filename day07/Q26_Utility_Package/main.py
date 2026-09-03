from utilities.calculator import add
from utilities.calculator import multiply

from utilities.student import student_info

from utilities.employee import employee_info


print("Addition =", add(10, 20))

print("Multiplication =", multiply(10, 20))


student_info(
    "Sneha",
    20,
    "MCA"
)


employee_info(
    "Rahul",
    30000
)