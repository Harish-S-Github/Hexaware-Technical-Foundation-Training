class SalaryCalculation:
    def __init__(self, name, basic_pay, hra, acs, etc, in_notice_period=False):
        self.employee = name
        self.basic_pay = basic_pay
        self.hra = hra
        self.acs = acs
        self.etc = etc
        self.in_notice_period = in_notice_period
        self.total_salary = 0

    def calculate_salary(self):
        self.total_salary = self.basic_pay + self.hra + self.acs + self.etc
        print(f"{self.employee}'s Total Salary: ₹{self.total_salary}")
        return self.total_salary

    def salary_after_hike(self, hike_percent):
        if self.total_salary == 0:
            self.calculate_salary()
        hiked_salary = self.total_salary + (self.total_salary * hike_percent / 100)
        print(f"{self.employee}'s Salary after {hike_percent}% hike: ₹{hiked_salary}")
        return hiked_salary

    def something_not_ok(self):
        print(f"{self.employee} has reported an issue. Please check with HR or Payroll.")

    def notice_period(self):
        if self.in_notice_period:
            print(f"{self.employee} is currently serving the notice period.")
        else:
            print(f"{self.employee} is a regular employee.")