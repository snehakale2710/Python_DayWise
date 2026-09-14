# Q41. Create a VotingSystem class with private __candidate_votes.
# Add methods to cast a vote and display vote counts.

class VotingSystem:
    def __init__(self):
        self.__candidate_votes = {}

    def cast_vote(self, candidate):
        if candidate in self.__candidate_votes:
            self.__candidate_votes[candidate] += 1
        else:
            self.__candidate_votes[candidate] = 1

    def display_votes(self):
        print(self.__candidate_votes)


v = VotingSystem()
v.cast_vote("A")
v.cast_vote("B")
v.cast_vote("A")
v.display_votes()


# Q42. Create a Quiz class with private __score.
# Add methods to add marks for correct answers and display the final score.

class Quiz:
    def __init__(self):
        self.__score = 0

    def add_marks(self, marks):
        self.__score += marks

    def display_score(self):
        print("Score:", self.__score)


q = Quiz()
q.add_marks(5)
q.add_marks(10)
q.display_score()


# Q43. Create a GamePlayer class with private __health and __score.
# Add methods to increase score and reduce health.

class GamePlayer:
    def __init__(self):
        self.__health = 100
        self.__score = 0

    def increase_score(self, points):
        self.__score += points

    def reduce_health(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0

    def display(self):
        print("Health:", self.__health)
        print("Score:", self.__score)


p = GamePlayer()
p.increase_score(50)
p.reduce_health(20)
p.display()


# Q44. Create a FitnessTracker class with private __steps.
# Add methods to add daily steps and calculate whether the daily goal was achieved.

class FitnessTracker:
    def __init__(self):
        self.__steps = 0

    def add_steps(self, steps):
        self.__steps += steps

    def goal_achieved(self):
        return self.__steps >= 10000

    def display(self):
        print("Steps:", self.__steps)
        print("Goal Achieved:", self.goal_achieved())


f = FitnessTracker()
f.add_steps(12000)
f.display()


# Q45. Create a HotelRoom class with private __room_number and __is_booked.
# Add booking and checkout methods.

class HotelRoom:
    def __init__(self, room_number):
        self.__room_number = room_number
        self.__is_booked = False

    def book(self):
        if not self.__is_booked:
            self.__is_booked = True
            print("Room booked")
        else:
            print("Room already booked")

    def checkout(self):
        if self.__is_booked:
            self.__is_booked = False
            print("Checkout successful")
        else:
            print("Room is not booked")

    def display(self):
        print("Room:", self.__room_number)
        print("Booked:", self.__is_booked)


room = HotelRoom(101)
room.book()
room.display()
room.checkout()


# Q46. Create a ParkingSlot class with private __slot_number and __vehicle_number.
# Add park() and remove_vehicle() methods.

class ParkingSlot:
    def __init__(self, slot_number):
        self.__slot_number = slot_number
        self.__vehicle_number = None

    def park(self, vehicle_number):
        if self.__vehicle_number is None:
            self.__vehicle_number = vehicle_number
            print("Vehicle parked")
        else:
            print("Slot already occupied")

    def remove_vehicle(self):
        if self.__vehicle_number is not None:
            self.__vehicle_number = None
            print("Vehicle removed")
        else:
            print("Slot is empty")


slot = ParkingSlot(1)
slot.park("MH45AB1234")
slot.remove_vehicle()


# Q47. Create a DeliveryOrder class with private __order_id, __address, and __amount.
# Add methods to update address and calculate delivery charge.

class DeliveryOrder:
    def __init__(self, order_id, address, amount):
        self.__order_id = order_id
        self.__address = address
        self.__amount = amount

    def update_address(self, address):
        self.__address = address

    def delivery_charge(self):
        return 50

    def display(self):
        print("Order ID:", self.__order_id)
        print("Address:", self.__address)
        print("Amount:", self.__amount)
        print("Delivery Charge:", self.delivery_charge())


d = DeliveryOrder(101, "Pune", 500)
d.update_address("Mumbai")
d.display()


# Q48. Create a Subscription class with private __plan and __price.
# Add methods to upgrade the plan and display subscription details.

class Subscription:
    def __init__(self, plan, price):
        self.__plan = plan
        self.__price = price

    def upgrade(self, plan, price):
        self.__plan = plan
        self.__price = price

    def display(self):
        print("Plan:", self.__plan)
        print("Price:", self.__price)


s = Subscription("Basic", 199)
s.upgrade("Premium", 499)
s.display()


# Q49. Create a LoanAccount class with private __principal and __interest_rate.
# Add a method to calculate EMI using a suitable formula.

class LoanAccount:
    def __init__(self, principal, interest_rate, months):
        self.__principal = principal
        self.__interest_rate = interest_rate
        self.__months = months

    def calculate_emi(self):
        r = self.__interest_rate / (12 * 100)
        n = self.__months

        if r == 0:
            return self.__principal / n

        emi = (self.__principal * r * (1 + r) ** n) / ((1 + r) ** n - 1)
        return emi


loan = LoanAccount(100000, 10, 12)
print("EMI:", loan.calculate_emi())


# Q50. Create a SecureBankAccount class where balance is private
# and withdrawals are allowed only after PIN verification.

class SecureBankAccount:
    def __init__(self, balance, pin):
        self.__balance = balance
        self.__pin = pin

    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful")
            else:
                print("Insufficient balance")
        else:
            print("Invalid PIN")

    def display_balance(self):
        print("Balance:", self.__balance)


account = SecureBankAccount(5000, 1234)
account.withdraw(1000, 1234)
account.display_balance()


# Q51. Create an EmployeePayroll class with private salary components.
# Calculate gross salary and net salary after deductions.

class EmployeePayroll:
    def __init__(self, basic, hra, da, deduction):
        self.__basic = basic
        self.__hra = hra
        self.__da = da
        self.__deduction = deduction

    def gross_salary(self):
        return self.__basic + self.__hra + self.__da

    def net_salary(self):
        return self.gross_salary() - self.__deduction


payroll = EmployeePayroll(20000, 5000, 3000, 2000)
print("Gross Salary:", payroll.gross_salary())
print("Net Salary:", payroll.net_salary())


# Q52. Create a SmartPhone class with private battery percentage.
# Add charge() and use_phone() methods and prevent invalid battery values.

class SmartPhone:
    def __init__(self, battery):
        self.__battery = max(0, min(battery, 100))

    def charge(self, percentage):
        self.__battery += percentage
        if self.__battery > 100:
            self.__battery = 100

    def use_phone(self, percentage):
        self.__battery -= percentage
        if self.__battery < 0:
            self.__battery = 0

    def display(self):
        print("Battery:", self.__battery, "%")


phone = SmartPhone(50)
phone.charge(30)
phone.use_phone(20)
phone.display()


# Q53. Create a WaterTank class with private __capacity and __current_level.
# Add fill() and use_water() methods with validation.

class WaterTank:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__current_level = 0

    def fill(self, amount):
        if amount > 0:
            self.__current_level += amount
            if self.__current_level > self.__capacity:
                self.__current_level = self.__capacity

    def use_water(self, amount):
        if amount > 0 and amount <= self.__current_level:
            self.__current_level -= amount
        else:
            print("Invalid water usage")

    def display(self):
        print("Water Level:", self.__current_level)


tank = WaterTank(1000)
tank.fill(500)
tank.use_water(200)
tank.display()


# Q54. Create a SchoolFee class with private __total_fee and __paid_fee.
# Add methods to pay fees and calculate remaining fees.

class SchoolFee:
    def __init__(self, total_fee):
        self.__total_fee = total_fee
        self.__paid_fee = 0

    def pay_fee(self, amount):
        if amount > 0 and self.__paid_fee + amount <= self.__total_fee:
            self.__paid_fee += amount

    def remaining_fee(self):
        return self.__total_fee - self.__paid_fee


fee = SchoolFee(50000)
fee.pay_fee(20000)
print("Remaining Fee:", fee.remaining_fee())


# Q55. Create a TravelWallet class with private __balance and __currency.
# Add methods to add money and spend money.

class TravelWallet:
    def __init__(self, balance, currency):
        self.__balance = balance
        self.__currency = currency

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount

    def spend_money(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def display(self):
        print("Balance:", self.__balance, self.__currency)


wallet = TravelWallet(1000, "INR")
wallet.add_money(500)
wallet.spend_money(200)
wallet.display()


# Q56. Create a PasswordManager class with private __password.
# Add methods to validate password length and change the password.

class PasswordManager:
    def __init__(self, password):
        self.__password = password

    def validate_password(self):
        return len(self.__password) >= 8

    def change_password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password
            print("Password changed")
        else:
            print("Password must contain at least 8 characters")


pm = PasswordManager("password123")
print(pm.validate_password())
pm.change_password("newpass123")


# Q57. Create a DigitalCounter class with private __count.
# Add increment(), decrement(), and reset() methods; count must never be negative.

class DigitalCounter:
    def __init__(self):
        self.__count = 0

    def increment(self):
        self.__count += 1

    def decrement(self):
        if self.__count > 0:
            self.__count -= 1

    def reset(self):
        self.__count = 0

    def display(self):
        print("Count:", self.__count)


counter = DigitalCounter()
counter.increment()
counter.increment()
counter.decrement()
counter.display()
counter.reset()


# Q58. Create a Company class with private employee count.
# Add methods to join and leave the company while maintaining a valid count.

class Company:
    def __init__(self):
        self.__employee_count = 0

    def join(self):
        self.__employee_count += 1

    def leave(self):
        if self.__employee_count > 0:
            self.__employee_count -= 1

    def display(self):
        print("Employees:", self.__employee_count)


company = Company()
company.join()
company.join()
company.leave()
company.display()


# Q59. Create a BankTransaction class with private transaction amount and type.
# Validate that transaction amount is positive.

class BankTransaction:
    def __init__(self, amount, transaction_type):
        if amount > 0:
            self.__amount = amount
        else:
            self.__amount = 0

        self.__transaction_type = transaction_type

    def display(self):
        print("Amount:", self.__amount)
        print("Type:", self.__transaction_type)


transaction = BankTransaction(1000, "Credit")
transaction.display()


# Q60. Create a SecureStudent class with private student ID and marks.
# Provide public methods for safe access and modification.

class SecureStudent:
    def __init__(self, student_id, marks):
        self.__student_id = student_id
        self.__marks = marks

    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks


student = SecureStudent(101, 80)
print(student.get_student_id())
student.set_marks(90)
print(student.get_marks())


# Q61. Create a ProductStock class with private stock quantity and minimum stock level.
# Display a low-stock warning when required.

class ProductStock:
    def __init__(self, quantity, minimum_stock):
        self.__quantity = quantity
        self.__minimum_stock = minimum_stock

    def add_stock(self, quantity):
        self.__quantity += quantity

    def sell(self, quantity):
        if quantity <= self.__quantity:
            self.__quantity -= quantity

    def display(self):
        print("Stock:", self.__quantity)
        if self.__quantity <= self.__minimum_stock:
            print("Low Stock Warning")


stock = ProductStock(20, 5)
stock.sell(16)
stock.display()


# Q62. Create a CabBooking class with private distance and fare.
# Calculate fare using base fare plus per-kilometer charge.

class CabBooking:
    def __init__(self, distance):
        self.__distance = distance

    def calculate_fare(self):
        base_fare = 50
        per_km = 15
        return base_fare + self.__distance * per_km


cab = CabBooking(10)
print("Fare:", cab.calculate_fare())


# Q63. Create a SalarySlip class with private employee details and salary.
# Display a formatted salary slip using public methods.

class SalarySlip:
    def __init__(self, name, employee_id, salary):
        self.__name = name
        self.__employee_id = employee_id
        self.__salary = salary

    def display(self):
        print("----- Salary Slip -----")
        print("Name:", self.__name)
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)


slip = SalarySlip("Sneha", 101, 30000)
slip.display()


# Q64. Create a DigitalLibrary class with private book list.
# Add methods to borrow and return books without directly exposing the list.

class DigitalLibrary:
    def __init__(self):
        self.__books = ["Python", "Java", "C++"]

    def borrow(self, book):
        if book in self.__books:
            self.__books.remove(book)
            print("Book borrowed")
        else:
            print("Book not available")

    def return_book(self, book):
        self.__books.append(book)
        print("Book returned")


library = DigitalLibrary()
library.borrow("Python")
library.return_book("Python")


# Q65. Create a Membership class with private member status.
# Allow activation and deactivation only through public methods.

class Membership:
    def __init__(self):
        self.__status = False

    def activate(self):
        self.__status = True

    def deactivate(self):
        self.__status = False

    def display(self):
        print("Membership Active:", self.__status)


member = Membership()
member.activate()
member.display()
member.deactivate()


# Q66. Create a SecureATM class with private PIN, balance, and transaction count.
# Allow only a limited number of failed PIN attempts.

class SecureATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance
        self.__failed_attempts = 0

    def withdraw(self, amount, pin):
        if self.__failed_attempts >= 3:
            print("ATM blocked")
            return

        if pin != self.__pin:
            self.__failed_attempts += 1
            print("Wrong PIN")
            return

        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Balance:", self.__balance)


atm = SecureATM(1234, 10000)
atm.withdraw(2000, 1234)
atm.display_balance()


# Q67. Create a SchoolAttendance class with private attendance percentage.
# Allow attendance updates only between 0 and 100.

class SchoolAttendance:
    def __init__(self, attendance):
        self.__attendance = 0
        self.update_attendance(attendance)

    def update_attendance(self, attendance):
        if 0 <= attendance <= 100:
            self.__attendance = attendance
        else:
            print("Invalid attendance")

    def display(self):
        print("Attendance:", self.__attendance, "%")


attendance = SchoolAttendance(85)
attendance.update_attendance(90)
attendance.display()


# Q68. Create a ProductDiscount class with private price and discount.
# Validate discount between 0 and 100 and calculate final price.

class ProductDiscount:
    def __init__(self, price, discount):
        self.__price = price
        self.__discount = 0
        self.set_discount(discount)

    def set_discount(self, discount):
        if 0 <= discount <= 100:
            self.__discount = discount

    def final_price(self):
        return self.__price - (self.__price * self.__discount / 100)


product = ProductDiscount(1000, 20)
print("Final Price:", product.final_price())


# Q69. Create a Loan class with private loan amount and tenure.
# Add methods to calculate total interest and repayment amount.

class Loan:
    def __init__(self, amount, tenure):
        self.__amount = amount
        self.__tenure = tenure

    def total_interest(self):
        rate = 10
        return self.__amount * rate * self.__tenure / 100

    def repayment_amount(self):
        return self.__amount + self.total_interest()


loan = Loan(50000, 2)
print("Interest:", loan.total_interest())
print("Repayment:", loan.repayment_amount())


# Q70. Create a MedicalBill class with private consultation, medicine, and test charges.
# Calculate the final bill.

class MedicalBill:
    def __init__(self, consultation, medicine, test):
        self.__consultation = consultation
        self.__medicine = medicine
        self.__test = test

    def final_bill(self):
        return self.__consultation + self.__medicine + self.__test


bill = MedicalBill(500, 1000, 1500)
print("Final Bill:", bill.final_bill())


# Q71. Create a SalaryIncrement class with private salary.
# Add a method to increase salary by a percentage and display the new salary.

class SalaryIncrement:
    def __init__(self, salary):
        self.__salary = salary

    def increase_salary(self, percentage):
        self.__salary += self.__salary * percentage / 100

    def display(self):
        print("New Salary:", self.__salary)


salary = SalaryIncrement(30000)
salary.increase_salary(10)
salary.display()


# Q72. Create a FoodOrder class with private order total.
# Add items and apply coupon discounts through public methods.

class FoodOrder:
    def __init__(self):
        self.__order_total = 0

    def add_item(self, price):
        if price > 0:
            self.__order_total += price

    def apply_coupon(self, discount):
        if 0 <= discount <= 100:
            self.__order_total -= self.__order_total * discount / 100

    def display(self):
        print("Order Total:", self.__order_total)


food = FoodOrder()
food.add_item(500)
food.add_item(300)
food.apply_coupon(10)
food.display()


# Q73. Create a BusPass class with private passenger details and validity days.
# Add a renew() method and display remaining validity.

class BusPass:
    def __init__(self, passenger_name, validity_days):
        self.__passenger_name = passenger_name
        self.__validity_days = validity_days

    def renew(self, days):
        if days > 0:
            self.__validity_days += days

    def display(self):
        print("Passenger:", self.__passenger_name)
        print("Validity Days:", self.__validity_days)


bus_pass = BusPass("Sneha", 30)
bus_pass.renew(30)
bus_pass.display()


# Q74. Create a SecureProfile class with private email and phone.
# Add public methods to update them after validation.

class SecureProfile:
    def __init__(self, email, phone):
        self.__email = email
        self.__phone = phone

    def update_email(self, email):
        if "@" in email:
            self.__email = email
        else:
            print("Invalid email")

    def update_phone(self, phone):
        if str(phone).isdigit() and len(str(phone)) == 10:
            self.__phone = phone
        else:
            print("Invalid phone number")

    def display(self):
        print("Email:", self.__email)
        print("Phone:", self.__phone)


profile = SecureProfile("sneha@gmail.com", "9876543210")
profile.update_email("new@gmail.com")
profile.update_phone("9123456789")
profile.display()


# Q75. Create a BankStatement class with private transactions.
# Add credit and debit methods and a public method to display the statement.

class BankStatement:
    def __init__(self):
        self.__transactions = []

    def credit(self, amount):
        if amount > 0:
            self.__transactions.append(("Credit", amount))

    def debit(self, amount):
        if amount > 0:
            self.__transactions.append(("Debit", amount))

    def display(self):
        for transaction in self.__transactions:
            print(transaction)


statement = BankStatement()
statement.credit(5000)
statement.debit(1000)
statement.display()


# Q76. Create a RentalCar class with private daily rent and rented days.
# Calculate total rent with a late-return penalty.

class RentalCar:
    def __init__(self, daily_rent, rented_days):
        self.__daily_rent = daily_rent
        self.__rented_days = rented_days

    def calculate_rent(self, late_days):
        rent = self.__daily_rent * self.__rented_days
        penalty = late_days * 500
        return rent + penalty


car = RentalCar(1000, 5)
print("Total Rent:", car.calculate_rent(2))


# Q77. Create a StockMarketAccount class with private cash balance and holdings.
# Add buy and sell methods with validation.

class StockMarketAccount:
    def __init__(self, cash):
        self.__cash = cash
        self.__holdings = 0

    def buy(self, quantity, price):
        total = quantity * price
        if total <= self.__cash:
            self.__cash -= total
            self.__holdings += quantity
            print("Stock bought")
        else:
            print("Insufficient cash")

    def sell(self, quantity, price):
        if quantity <= self.__holdings:
            self.__holdings -= quantity
            self.__cash += quantity * price
            print("Stock sold")
        else:
            print("Not enough holdings")

    def display(self):
        print("Cash:", self.__cash)
        print("Holdings:", self.__holdings)


stock_account = StockMarketAccount(10000)
stock_account.buy(10, 500)
stock_account.sell(2, 600)
stock_account.display()


# Q78. Create a Classroom class with private student list and capacity.
# Prevent adding students after capacity is reached.

class Classroom:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__students = []

    def add_student(self, name):
        if len(self.__students) < self.__capacity:
            self.__students.append(name)
        else:
            print("Classroom capacity reached")

    def display(self):
        print("Students:", self.__students)


classroom = Classroom(2)
classroom.add_student("Amit")
classroom.add_student("Sneha")
classroom.add_student("Rahul")
classroom.display()


# Q79. Create a ResultManagement class with private student marks dictionary.
# Add methods to safely update marks and calculate averages.

class ResultManagement:
    def __init__(self):
        self.__marks = {}

    def update_marks(self, name, marks):
        if 0 <= marks <= 100:
            self.__marks[name] = marks

    def calculate_average(self):
        if len(self.__marks) == 0:
            return 0
        return sum(self.__marks.values()) / len(self.__marks)


result = ResultManagement()
result.update_marks("Amit", 80)
result.update_marks("Sneha", 90)
print("Average:", result.calculate_average())


# Q80. Create a SecureEmployee class with private employee salary.
# Allow salary access only through a getter and update through a validated setter.

class SecureEmployee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary


employee = SecureEmployee(30000)
print(employee.get_salary())
employee.set_salary(35000)
print(employee.get_salary())


# Q81. Create a PaymentGateway class with private payment status and amount.
# Add methods to initiate, complete, and cancel payment.

class PaymentGateway:
    def __init__(self):
        self.__payment_status = "Not Started"
        self.__amount = 0

    def initiate(self, amount):
        if amount > 0:
            self.__amount = amount
            self.__payment_status = "Initiated"

    def complete(self):
        if self.__payment_status == "Initiated":
            self.__payment_status = "Completed"

    def cancel(self):
        if self.__payment_status == "Initiated":
            self.__payment_status = "Cancelled"

    def display(self):
        print("Amount:", self.__amount)
        print("Status:", self.__payment_status)


payment = PaymentGateway()
payment.initiate(2000)
payment.complete()
payment.display()


# Q82. Create a Recharge class with private mobile number and amount.
# Validate the number and prevent invalid recharge amounts.

class Recharge:
    def __init__(self, mobile_number, amount):
        self.__mobile_number = mobile_number
        self.__amount = amount

    def recharge(self):
        phone = str(self.__mobile_number)

        if len(phone) == 10 and phone.isdigit() and self.__amount > 0:
            print("Recharge successful")
        else:
            print("Invalid recharge details")


recharge = Recharge("9876543210", 299)
recharge.recharge()


# Q83. Create a Courier class with private weight and distance.
# Calculate shipping cost based on both values.

class Courier:
    def __init__(self, weight, distance):
        self.__weight = weight
        self.__distance = distance

    def shipping_cost(self):
        return (self.__weight * 50) + (self.__distance * 5)


courier = Courier(2, 100)
print("Shipping Cost:", courier.shipping_cost())


# Q84. Create a UtilityBill class with private customer ID and amount.
# Add methods to apply late fees and display the final amount.

class UtilityBill:
    def __init__(self, customer_id, amount):
        self.__customer_id = customer_id
        self.__amount = amount

    def apply_late_fee(self, fee):
        if fee > 0:
            self.__amount += fee

    def display(self):
        print("Customer ID:", self.__customer_id)
        print("Final Amount:", self.__amount)


utility = UtilityBill(101, 1500)
utility.apply_late_fee(100)
utility.display()


# Q85. Create a BankInterest class with private principal, rate, and time.
# Calculate simple and compound interest through public methods.

class BankInterest:
    def __init__(self, principal, rate, time):
        self.__principal = principal
        self.__rate = rate
        self.__time = time

    def simple_interest(self):
        return (self.__principal * self.__rate * self.__time) / 100

    def compound_interest(self):
        amount = self.__principal * (1 + self.__rate / 100) ** self.__time
        return amount - self.__principal


interest = BankInterest(10000, 10, 2)

print("Simple Interest:", interest.simple_interest())
print("Compound Interest:", interest.compound_interest())