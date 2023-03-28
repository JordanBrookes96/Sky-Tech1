def addition():
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    result = num1 + num2
    print("Result of sum is:", result)


def subtraction():
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    result = num1 - num2
    print("Result of sum is:", result)


def division():
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    result = num1 / num2
    print("Result of sum is:", result)


def maths(ch):
    if ch == 1:
        addition()
        print("addition function called")
    if ch == 2:
        subtraction()
        print("subtraction function called")
    if ch == 3:
        division()
        print("division function called")


try:
    maths(3)
    print("Sky Limited")
except ZeroDivisionError:
    print("You can not divide a number by zero")
except ValueError:
    print("Please enter digits only")
