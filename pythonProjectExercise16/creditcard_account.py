from library import CreditCardAccount

print("")
credit_card_account = CreditCardAccount(123456789, 0, 5000)
print("-----------------------------")
credit_card_account.charge(2000)
print("-----------------------------")
credit_card_account.make_payment(1000)
print("-----------------------------")
credit_card_account.charge(4000)
print("-----------------------------")
credit_card_account.charge(2000)
