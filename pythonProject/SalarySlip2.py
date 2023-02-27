name = input("Enter the employee name:")
salary = float(input(name+"'s Salary:"))

if salary >= 2000:
    tax = salary * 21/100
    taxrate = "21%"
else:
    tax = salary * 15/100
    taxrate = "15%"

net = salary - tax
print("--------------------------")
print("Tax Rate:",taxrate)
print("--------------------------")
print("Tax Calculated is:",tax)
print("--------------------------")
print("Net Salary:",net)