def tax(salary=1000, taxrate=17):
    t = salary * taxrate / 100
    net = salary - t
    print("Tax Rate Is:", taxrate)
    print("Calculated tax is:", t)
    print("Net Salary Is:", net)


tax(1000, 31)
print("--------------")
tax(1000)
print("--------------")
tax()
