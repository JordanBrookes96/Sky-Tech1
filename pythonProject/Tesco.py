product = input("Enter the name of your product:")
quantity = input("Enter the quantity:")
price = input ("Enter the unit price:")

bill = int(quantity) * float(price)

print("-------------------------------")
print("Welcome To Tesco Super Stores")
print("-------------------------------")
print("Product Bought:",product)
print("Quantity:",quantity)
print("Unit Price:",price)
print("-------------------------------")
print("Your Bill is",bill)