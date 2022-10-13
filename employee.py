"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary=0, hours=0, payPerHour=0, commission="none", numberOfCommissions=1, commissionPay=0):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.payPerHour = payPerHour
        self.commission = commission
        self.numberOfCommissions = numberOfCommissions
        self.commissionPay = commissionPay

    def get_pay(self):
        self.totalPay = self.salary + (self.hours * self.payPerHour) + (self.numberOfCommissions * self.commissionPay)
        return self.totalPay

    def __str__(self):
        self.breakdown = self.name + " works on a "
        if self.hours > 0 and self.salary == 0:
            self.breakdown = self.breakdown + "contract of " + str(self.hours) + " hours at " + str(self.payPerHour) + "/hour"
        elif self.salary > 0 and self.hours == 0:
            self.breakdown = self.breakdown + "monthly salary of " + str(self.salary)
        else:
            self.breakdown = ""
        if self.commission == "contract":
            self.breakdown = self.breakdown + " and receives a commission for " + str(self.numberOfCommissions) + " contract(s) at " + str(self.commissionPay) + "/contract"
        elif self.commission == "bonus":
            self.breakdown = self.breakdown + " and receives a bonus comission of " + str(self.commissionPay)
        self.breakdown = self.breakdown + ". Their total pay is " + str(self.totalPay) + "."
        return self.breakdown


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("Billie", salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee("Charlie", hours=100, payPerHour=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee("Renee", salary=3000, commission="contract", numberOfCommissions=4, commissionPay=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee("Jan", hours=150, payPerHour=25, commission="contract", numberOfCommissions=3, commissionPay=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee("Robbie", salary=2000, commission="bonus", commissionPay=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee("Ariel", hours=120, payPerHour=30, commission="bonus", commissionPay=600)

billie.get_pay()
charlie.get_pay()
renee.get_pay()
jan.get_pay()
robbie.get_pay()
ariel.get_pay()
print(billie)
print(charlie)
print(renee)
print(jan)
print(robbie)
print(ariel)