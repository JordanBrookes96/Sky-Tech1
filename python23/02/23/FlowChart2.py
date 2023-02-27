total=0
ch = "y"

while ch=="y" or ch=="Y" or ch=="YES":
    T = int(input("Enter Employees Salary:"))
    total = total + T
    ch = input("......Do You Want To Enter Another Salary: ")
print("Total Amount Of Salaries:", total)
