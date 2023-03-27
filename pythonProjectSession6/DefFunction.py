def tax(salary1):
    t = salary1*21/100
    return t


name = input("Enter Your Name:")
salary = int(input("Enter Your Salary:"))

net = salary - tax(salary)
print("Tax Calculated is", tax(salary))
print("Net Salary Is:", net)

