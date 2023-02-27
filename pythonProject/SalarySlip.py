name = input("Enter the employee name:")
salary = input(name+"'s Salary:")

if float(salary) >= 2000:
    tax = float(salary) * 21/100
    taxrate = "21%"
else:
    tax = float(salary) * 15/100
    taxrate = "15%"

net = float(salary) - tax
print("--------------------------")
print("Tax Rate:",taxrate)
print("--------------------------")
print("Tax Calculated is:",tax)
print("--------------------------")
print("Net Salary:",net)