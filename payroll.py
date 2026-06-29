class Employee:
    def __init__(self, emp_id, name, basic_salary, hra, bonus, overtime, tax, pf, other_deductions):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        self.hra = hra
        self.bonus = bonus
        self.overtime = overtime
        self.tax = tax
        self.pf = pf
        self.other_deductions = other_deductions

    def calculate_gross_salary(self):
        return self.basic_salary + self.hra + self.bonus + self.overtime

    def calculate_net_salary(self):
        gross = self.calculate_gross_salary()
        deductions = self.tax + self.pf + self.other_deductions
        return gross - deductions

    def generate_payslip(self):
        gross = self.calculate_gross_salary()
        net = self.calculate_net_salary()

        print("\n========== PAYSLIP ==========")
        print("Employee ID :", self.emp_id)
        print("Employee Name :", self.name)
        print("-----------------------------")
        print(f"Basic Salary      : ₹{self.basic_salary}")
        print(f"HRA               : ₹{self.hra}")
        print(f"Bonus             : ₹{self.bonus}")
        print(f"Overtime          : ₹{self.overtime}")
        print("-----------------------------")
        print(f"Gross Salary      : ₹{gross}")
        print(f"Tax Deduction     : ₹{self.tax}")
        print(f"PF Deduction      : ₹{self.pf}")
        print(f"Other Deductions  : ₹{self.other_deductions}")
        print("-----------------------------")
        print(f"Net Salary        : ₹{net}")
        print("=============================")


emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))
hra = float(input("Enter HRA: "))
bonus = float(input("Enter Bonus: "))
overtime = float(input("Enter Overtime Amount: "))
tax = float(input("Enter Tax Deduction: "))
pf = float(input("Enter PF Deduction: "))
other_deductions = float(input("Enter Other Deductions: "))

employee = Employee(
    emp_id,
    name,
    basic_salary,
    hra,
    bonus,
    overtime,
    tax,
    pf,
    other_deductions
)

employee.generate_payslip()