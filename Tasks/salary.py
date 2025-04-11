import  modu as sc

# 1. Normal Employee
emp1 = sc.SalaryCalculation("Anand", basic_pay=30000, hra=10000, acs=5000, etc=3000)
emp1.calculate_salary()
emp1.salary_after_hike(10)
emp1.notice_period()

print()

# 2. Employee with a Very Good Hike
emp2 = sc.SalaryCalculation("Priya", basic_pay=35000, hra=15000, acs=7000, etc=4000)
emp2.calculate_salary()
emp2.salary_after_hike(50)  # Very good hike
emp2.notice_period()

print()

# 3. Employee in Notice Period
emp3 = sc.SalaryCalculation("Ravi", basic_pay=25000, hra=8000, acs=3000, etc=2000, in_notice_period=True)
emp3.calculate_salary()
emp3.salary_after_hike(5)
emp3.notice_period()

emp3.something_not_ok()
