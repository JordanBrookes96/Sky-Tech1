def message(name):
    print("Hello:", name)

def addition(num1, num2):
    result=num1+num2
    print("The Result Is:", result)

def Payslip(name, salary):
    if salary >=2000:
        tax=salary*21/100
    else:
        tax=salary*15/100
    net=salary-tax
    print("Employees Name:", name)
    print("Basic Salary:", salary)
    print("Tax Calculated is:", tax)
    print("Net Salary:", net)

message("Jordan")

print("--------------------")

message("John")

print("--------------------")

addition(100, 50)

print("--------------------")

n=input("Enter The Name Of The Employee:")
s=int(input("Enter Salary:"))
Payslip(n, s)

