def tax(salary):
    if salary >= 2000:
        tax = salary * 21 / 100
    else:
        tax = salary * 15 / 100
    return tax


def payslip(name, salary):
    net = salary - tax(salary)
    print("Employees Name:", name)
    print("Basic Salary:", salary)
    print("Tax Calculated Is:", tax(salary))
    print("Net Salary", net)


payslip("Name", 1000)
