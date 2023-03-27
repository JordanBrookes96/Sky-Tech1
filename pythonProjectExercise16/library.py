class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print(f"Your account balance is £{self.balance}")

    def deposit(self):
        amount = int(input("How much would you like to deposit: "))
        self.balance += amount
        print(
            f"You've successfully deposited £{amount} \n"
            f"Your new balance is £{self.balance}"
        )

    def withdraw(self):
        amount = int(input("How much would you like to withdraw: "))
        print(f"You would like to withdraw £{amount}")
        if self.balance - amount >= 0:
            self.balance -= amount
            print(
                f"You withdrawal was successful \n"
                f"Your new account balance is £{self.balance}"
            )
        else:
            print(f"Insufficient funds")


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        print(
            f"At {self.interest_rate * 100}% interest, "
            f"you've gained £{self.balance * self.interest_rate} in interest."
        )
        self.balance += self.balance * self.interest_rate
        print(f"Savings account balance: £{self.balance}")


class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self):
        amount = int(input("How much would you like to withdraw: "))
        print(f"You would like to withdraw £{amount}")
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            print(f"Checking account balance: £{self.balance}")
        else:
            print("Insufficient funds")


class CreditCardAccount(Account):
    def __init__(self, account_number, balance, credit_limit):
        super().__init__(account_number, balance)
        self.credit_limit = credit_limit

    def charge(self, amount):
        if self.balance + amount <= self.credit_limit:
            self.balance += amount
            print(
                f"We have charged £{amount} to your card \n"
                f"Your new credit card balance is £{self.balance}"
            )
        else:
            print("Exceeded credit limit")

    def make_payment(self, amount):
        self.balance -= amount
        print(
            f"You've paid £{amount} into your Credit Card Account \n"
            f"Your new balance is £{self.balance}"
        )
