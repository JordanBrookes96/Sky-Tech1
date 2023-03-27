# Bank Account

class BankAccount:

    def __init__(self, AccountName, AccountNumber, AccountSortCode, AccountBalance):
        self.AccountName = AccountName
        self.__AccountNumber = AccountNumber
        self.AccountSortCode = AccountSortCode
        self.AccountBalance = AccountBalance

    def get_AccountNumber(self):
        return self.__AccountNumber

    def set_AccountNumber(self, AccountNumber):
        self.__AccountNumber = AccountNumber
