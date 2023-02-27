import getpass

password = 1996

MaxAttempts = 3

while MaxAttempts > 0:
    pin = int(getpass.getpass("Enter Your Pin:"))
    if pin == password:
        print("Balance is: £1000")
        break
    else:
        MaxAttempts -= 1
        if MaxAttempts == 0:
            print("Card Blocked!")
            break
        print("Incorrect Pin, Try Again")

# part 2 of ex10 remove input from line 8 and replace it with getpass.getpass and run in python console.