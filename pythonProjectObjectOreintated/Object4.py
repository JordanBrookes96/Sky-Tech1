class SalarySlip:
    name = ""
    salary = 0

    def tax(self):
        tax = self.salary * 21 / 100
        net = self.salary - tax
        print("Tax calculated is:", tax)
        print("Net salary is:", net)


Jordan = SalarySlip()
print("Jordan's Salary Is:")
Jordan.name = "Jordan"
Jordan.salary = 22000
Jordan.tax()
print("-------------------------")
Jay = SalarySlip()
print("Jay's Salary Is:")
Jay.name = "Jay"
Jay.salary = 15000
Jay.tax()
