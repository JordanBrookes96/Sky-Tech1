import getpass

correct_pin = 1988
max_attempts = 3

while max_attempts > 0:
    supplied_pin = int(getpass.getpass("Enter Your Pin:"))
    if supplied_pin == correct_pin:
        print("Pin Accepted")
        print("Your Balance is £2,500")
        break
    else:
        max_attempts -= 1
        if max_attempts == 0:
            print("CARD BLOCKED")
            break
        print("PIN DECLINED, Attempts Left:", max_attempts)
        print("Please Try Again")