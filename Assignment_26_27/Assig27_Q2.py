class BankAccount:

    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder :", self.Name)
        print("Current Balance :", self.Amount)

    def Deposit(self):
        Money = float(input("Enter amount to deposit : "))
        self.Amount = self.Amount + Money

    def Withdraw(self):
        Money = float(input("Enter amount to withdraw : "))

        if Money <= self.Amount:
            self.Amount = self.Amount - Money
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


Obj1 = BankAccount("Sakshi", 10000)
Obj2 = BankAccount("Dhana", 5000)

print("Object 1")
Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
print("Interest :", Obj1.CalculateInterest())
Obj1.Display()

print()

print("Object 2")
Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()
print("Interest :", Obj2.CalculateInterest())
Obj2.Display()