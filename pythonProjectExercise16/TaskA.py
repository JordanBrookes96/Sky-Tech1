class Person:
    # Constructors - This is a function that gets called automatically when you create the object.
    # Below it will ask for 3 variables and then assign them automatically.
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def details(self):
        print(
            f"Name : {self.name} \n"
            f"Email : {self.email} \n"
            f"Address : {self.address}"
        )


# Inheritance - This is when one class inherits attributes from its parent class.
# Below Employee is inheriting everything from the Person class, so we don't have to define it again.
class Employee(Person):
    # Methods - These are basically functions inside a class
    def __init__(self, name, email, address, employee_number, salary):
        super().__init__(name, email, address)
        self.employee_number = employee_number
        self.__salary = salary

    # Encapsulation - Stops us being able to modify them from outside this class.
    # Properties - Allows us to access the encapsulated variables and change them.
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    # Polymorphism - Every class has a details function but this one does something different.
    # This is called polymorphism so person.details is different to employee.details.
    def details(self):
        super().details()
        print(f"Employee Number : {self.employee_number}")

    def tax_calculator(self):
        tax = self.__salary / 100 * 20
        net = self.__salary - tax
        print(
            f"Your salary is : {self.__salary} \n"
            f"Your tax is : {tax} \n"
            f"Your net is : {net}"
        )


class Customer(Person):
    def __init__(self, name, email, address, day, time):
        super().__init__(name, email, address)
        self.day = day
        self.time = time

    def details(self):
        super().details()

    def deliver(self):
        print(
            f"We will send you a copy of the receipt to {self.email} \n"
            f"We will attempt to deliver your bed on {self.day} at {self.time} o'clock. \n"
            f"If you're not in we will attempt to deliver them again the following day \n"
            f"Thank you for shopping with Jord's Beds Ltd."
        )


# System asking for persons details
print("")
print("Person's Details")
print("----------------")
person = Person("Jordan Brookes", "jordan.brookes@sky.uk", "Birmingham,UK")
person.details()

# If Person is part of company return employee details
print("")
print("Employee's Details")
print("----------------")
employee = Employee("Jordan Brookes", "jordan.brookes@sky.uk", "Birmingham,UK", 892547, 45000)
employee.details()
employee.tax_calculator()

# Entering customers details into system for mailing list
print("")
print("Customer's Details")
print("-------------------")
customer = Customer("Jordan Brookes", "jordan.brookes@sky.uk", "Birmingham,UK", "Monday", 5)
customer.details()
customer.deliver()
