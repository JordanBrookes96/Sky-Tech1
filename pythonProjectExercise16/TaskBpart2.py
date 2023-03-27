class BankAccount:
    def __init__(self, account_type, balance):
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__("Savings Account", balance)


class CheckingAccount(BankAccount):
    def __init__(self, balance):
        super().__init__("Checking Account", balance)


class MoneyMarketAccount(BankAccount):
    def __init__(self, balance):
        super().__init__("Money Market Account", balance)


class CertificateOfDeposit(BankAccount):
    def __init__(self, balance, term):
        super().__init__("Certificate of Deposit", balance)
        self.term = term


class IndividualRetirementAccount(BankAccount):
    def __init__(self, balance, age):
        super().__init__("Individual Retirement Account", balance)
        self.age = age


# Demonstration of the functionality of the Bank Account Hierarchy:

# Create a savings account with a balance of $1000
savings_account = SavingsAccount(1000)

# Deposit $500 into the savings account
savings_account.deposit(500)

# Withdraw $200 from the savings account
savings_account.withdraw(200)

# Create a checking account with a balance of $2000
checking_account = CheckingAccount(2000)

# Withdraw $300 from the checking account
checking_account.withdraw(300)

# Create a money market account with a balance of $5000
money_market_account = MoneyMarketAccount(5000)

# Withdraw $1000 from the money market account
money_market_account.withdraw(1000)

# Create a certificate of deposit with a balance of $10,000 and a term of 1 year
cd_account = CertificateOfDeposit(10000, 1)

# Attempt to withdraw $5000 from the CD before the term is up (this should fail)
cd_account.withdraw(5000)

# Create an individual retirement account with a balance of $50,000 and an age of 60
ira_account = IndividualRetirementAccount(50000, 60)

# Withdraw $10,000 from the IRA
ira_account.withdraw(10000)
