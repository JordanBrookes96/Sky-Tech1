from library import SavingsAccount

print("")
savings_account = SavingsAccount(123456789, 10000, 0.05)
print("-----------------------------")
savings_account.deposit()
print("-----------------------------")
savings_account.add_interest()
